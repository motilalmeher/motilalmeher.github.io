import os
from helper_components import evaluate_model
from helper_components import retrieve_best_run
from helper_components import split_data
from jinja2 import Template
import kfp
import kfp.dsl as dsl 
from kfp.components import func_to_container_op
from kfp.dsl.types import Dict
from kfp.dsl.types import GCPProjectID
from kfp.dsl.types import GCPRegion
from kfp.dsl.types import GCSPath
from kfp.dsl.types import String
from kfp.gcp import use_gcp_secret

# Defaults and environment settings
BASE_IMAGE = os.getenv('BASE_IMAGE')
TRAINER_IMAGE = os.getenv('TRAINER_IMAGE')
RUNTIME_VERSION = os.getenv('RUNTIME_VERSION')
PYTHON_VERSION = os.getenv('PYTHON_VERSION')
COMPONENT_URL_SEARCH_PREFIX = os.getenv('COMPONENT_URL_SEARCH_PREFIX')
USE_KFP_SA = os.getenv('USE_KFP_SA')

RAW_FILE_PATH = 'datasets/telecom_churn_data.csv'
PROCESS_FILE_PATH= 'datasets/processed_data/data.csv'
#TRAINING_FILE_PATH = 'datasets/training/data.csv'
#TESTING_FILE_PATH = 'datasets/testing/data.csv'
TRAINING_PROCESS_FILE_PATH = 'datasets/training_process/data.csv'
TESTING_PROCESS_FILE_PATH = 'datasets/testing_process/data.csv'

HYPERTUNE_SETTINGS = """
{
    "hyperparameters":  {
        "goal": "MAXIMIZE",
        "maxTrials": 4,
        "maxParallelTrials": 4,
        "hyperparameterMetricTag": "accuracy",
        "enableTrialEarlyStopping": True,
        "params": [
            {
                "parameterName": "C",
                "type": "DISCRETE",
                "discreteValues": [0.0001,0.001,0.01,0.1,1,10,100,1000]
            }
        ]
    }
}
"""




# Create component factories
component_store = kfp.components.ComponentStore(
    local_search_paths=None, url_search_prefixes=[COMPONENT_URL_SEARCH_PREFIX])

#bigquery_query_op = component_store.load_component('bigquery/query')
mlengine_train_op = component_store.load_component('ml_engine/train')

train_test_split_op = func_to_container_op(split_data, base_image=BASE_IMAGE)
retrieve_best_run_op = func_to_container_op(retrieve_best_run, base_image=BASE_IMAGE)
evaluate_model_op = func_to_container_op(evaluate_model, base_image=BASE_IMAGE)

mlengine_deploy_op = component_store.load_component('ml_engine/deploy')



#pipeline
@kfp.dsl.pipeline(
    name='Churn prediction',
    description='The pipeline training and deploying the Churn model. '
)
def churn_train(project_id,
                    region,
                    gcs_root,
                    evaluation_metric_name,
                    evaluation_metric_threshold,
                    model_id,
                    version_id,
                    replace_existing_version,
                    hypertune_settings=HYPERTUNE_SETTINGS,
                    dataset_location='US'):
    """Orchestrates training and deployment of an sklearn model."""

    
    #training_file_path = '{}/{}'.format(gcs_root, TRAINING_FILE_PATH)
    #testing_file_path = '{}/{}'.format(gcs_root, TESTING_FILE_PATH)
    
    
    raw_file_path= '{}/{}'.format(gcs_root,RAW_FILE_PATH)
    processed_file_path= '{}/{}'.format(gcs_root, PROCESS_FILE_PATH)
    
    data_preprocessor = dsl.ContainerOp(
        name='Load and preprocessing the raw data.',
        image=BASE_IMAGE,
        command=['python3', '-m', 'preprocess'],
        arguments=["--data_path", raw_file_path,
                   "--output_path", processed_file_path
                  ])
    
    training_processed_file_path= '{}/{}'.format(gcs_root, TRAINING_PROCESS_FILE_PATH)
    testing_processed_file_path= '{}/{}'.format(gcs_root, TESTING_PROCESS_FILE_PATH)
    
    data_split = train_test_split_op(dataset_path=processed_file_path,
                                     train_out_path=training_processed_file_path,
                                     test_out_path=testing_processed_file_path)
    
    
    model_filename='model.pkl'
    # Tune hyperparameters
    tune_args = [ '--model_filename',model_filename,
                  '--path',training_processed_file_path,
                  '--hptune', 'True']

    job_dir = '{}/{}/{}'.format(gcs_root, 'jobdir/hypertune',
                                kfp.dsl.RUN_ID_PLACEHOLDER)
    

    
    hypertune = mlengine_train_op(
        project_id=project_id,
        region=region,
        master_image_uri=TRAINER_IMAGE,
        job_dir=job_dir,
        args=tune_args,
        training_input=hypertune_settings)

    # Retrieve the best trial
    get_best_trial = retrieve_best_run_op(
            project_id, hypertune.outputs['job_id'])

    # Train the model on a combined training and validation datasets
    job_dir = '{}/{}/{}'.format(gcs_root, 'jobdir', kfp.dsl.RUN_ID_PLACEHOLDER)

    train_args = [
        '--model_filename', model_filename,
        '--path',training_processed_file_path,
        '--C',get_best_trial.outputs['C'],  
        '--hptune', 'False'
    ]

    train_model = mlengine_train_op(
        project_id=project_id,
        region=region,
        master_image_uri=TRAINER_IMAGE,
        job_dir=job_dir,
        args=train_args)
        
    
  
    # Evaluate the model on the testing split
    eval_model = evaluate_model_op(
        dataset_path=str(testing_processed_file_path),
        model_path=str(train_model.outputs['job_dir']),
        model_filename=model_filename,
        metric_name=evaluation_metric_name)
    
    #model_uri='{}/{}'.format(str(train_model.outputs['job_dir']),model_filename)
    # Deploy the model if the primary metric is better than threshold
    with kfp.dsl.Condition(eval_model.outputs['metric_value'] > evaluation_metric_threshold):
        deploy_model = mlengine_deploy_op(
        model_uri=train_model.outputs['job_dir'],
        project_id=project_id,
        model_id=model_id,
        version_id=version_id,
        runtime_version=RUNTIME_VERSION,
        python_version=PYTHON_VERSION,
        replace_existing_version=replace_existing_version)

    # Configure the pipeline to run using the service account defined
    # in the user-gcp-sa k8s secret
    if USE_KFP_SA == 'True':
        kfp.dsl.get_pipeline_conf().add_op_transformer(
              use_gcp_secret('user-gcp-sa'))
        
    
    ##################
    # Define dependencies
    ##################
    #train test data split after preprocess
    data_split.after(data_preprocessor)
    
    #hyperparameter tuning after data spliting
    hypertune.after(data_split)
    
    #get best parameter after hyperpaarmeter tuning
    get_best_trial.after(hypertune)
    
    #Final model train after getting best parameter
    train_model.after(get_best_trial)
    
    
    # evaluate model test data being preprocessed and final model being created
    eval_model.after(train_model)
    eval_model.after(data_split)
    
    # deploy model after model evaluation
    deploy_model.after(eval_model)
    
    
    
    
    
    # Disable caching
    data_preprocessor.execution_options.caching_strategy.max_cache_staleness = "P0D"
    data_split.execution_options.caching_strategy.max_cache_staleness = "P0D"
    hypertune.execution_options.caching_strategy.max_cache_staleness = "P0D"
    get_best_trial.execution_options.caching_strategy.max_cache_staleness = "P0D"
    train_model.execution_options.caching_strategy.max_cache_staleness = "P0D"
    
    eval_model.execution_options.caching_strategy.max_cache_staleness = "P0D"
    
    deploy_model.execution_options.caching_strategy.max_cache_staleness = "P0D"
        
        