import kfp
import kfp.dsl as dsl


MODEL_NAME = ''


@dsl.pipeline(
    name='churn scoring',
    description='This pipeline sends predictors to the churn model and stores the score.'
)
def pipeline(project_id,model_name=MODEL_NAME):
    
    predictions_task = dsl.ContainerOp(
        name='send-predictions',
        image= ,
        command=['python3', '-m', 'predict'],
        arguments=[
           '--model_name', model_name,
    
        ]
    )

    send_predictions_task.execution_options.caching_strategy.max_cache_staleness = "P0D"

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(pipeline, __file__ + '.yaml')
