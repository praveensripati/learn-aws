# Before running this make sure an SNS Topic is created
# CHANGE the TopicARN got from the console and the email address
# Notice that a new subscription would be created in the Management Console

import boto3

sns = boto3.client('sns', region_name='us-east-1')
response = sns.subscribe(
    TopicArn='arn:aws:sns:us-east-1:963880036659:my-topic',
    Protocol='email',
    Endpoint='ugetaws@gmail.com'
)

print(response)
