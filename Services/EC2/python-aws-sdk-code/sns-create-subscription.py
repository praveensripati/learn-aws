import boto3

sns = boto3.client('sns')
response = sns.subscribe(
    TopicArn='arn:aws:sns:us-east-1:963880036659:my-topic',
    Protocol='email',
    Endpoint='ugetaws@gmail.com'
)

print(response)
