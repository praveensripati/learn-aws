import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2', region_name='us-east-1')

try:
    # CHANGE
    # Grab the SG ID from the Console
    response = ec2.describe_security_groups(GroupIds=['sg-04fe0d799cc9dd1e2'])
    print(response)
except ClientError as e:
    print(e)