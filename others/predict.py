import os
import random
import argparse

import os
from googleapiclient import discovery

from utils import utils, db_connector


def predict(model_name, instances):
    
    service = discovery.build('ml', 'v1')
    name = 'projects/{}/models/{}'.format('projectmtna', model_name)
    

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()
    
    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']




def predict_and_store(model_name,data_path):
    
    df=pd.read_csv(data_path)
    dff=df.drop(columns=['mobile_number','churn'])
    
    x=[]
    for index, row in dff.iterrows():
        x.append(list(row.values))
    
    predictions = predict(model_name, instances)
    
    rows = []

    for idx, pred in enumerate(predictions):
        rows.append((int(df['mobile_number'][idx]), pred))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--model_name', required=True)
    args = parser.parse_args().__dict__

    model_name = args['model_name']
    
    predict_and_store(model_name)
    