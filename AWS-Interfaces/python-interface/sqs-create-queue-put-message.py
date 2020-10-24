import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='MyDemoQueue123',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)
print("CREATED A QUEUE")
print(response['QueueUrl'])

queue_url = response['QueueUrl']

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageBody=(
        'Transfer 1000USD FROM ACNT1 TO ACNT2'
    )
)
print("SENT A MESSAGE")
print(response['MessageId'])
