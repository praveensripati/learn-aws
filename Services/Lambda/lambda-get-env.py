import json
import os

def lambda_handler(event, context):

    env = os.getenv("ENV")
    print ("ENV = ", env)

    return {
        'statusCode': 200,
        'body': json.dumps('Got the environment in which I am in')
    }
