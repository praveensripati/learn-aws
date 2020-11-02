import boto3
from botocore.exceptions import ClientError
print('Loading function')

SENDER = "xyz@gmail.com"
RECIPIENT = "abc@gmail.com"
SUBJECT = "New User"
BODY_TEXT = "Hurray a new user has been created !!!!"

AWS_REGION = "us-east-1"
CHARSET = "UTF-8"


def lambda_handler(event, context):

    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER
        )

    # Error handling
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
