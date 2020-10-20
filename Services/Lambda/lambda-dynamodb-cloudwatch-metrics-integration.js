import boto3

def lambda_handler(event, context):

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Metrics')
response = table.get_item(Key = { 'Name': 'Users' })
connected = response['Item']['Connected']
print("Got the metrics from DynamoDB")

cloudwatch = boto3.client('cloudwatch')
response = cloudwatch.put_metric_data(
    MetricData = [
        {
            'MetricName': 'logged-in-users',
            'Unit': 'Count',
            'Value': int(connected)
        },
    ],
    Namespace = 'MyEcommerceApp'
)
print("Sent the metrics to CloudWatch")
