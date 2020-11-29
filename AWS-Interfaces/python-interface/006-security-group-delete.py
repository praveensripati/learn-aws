import boto3
from botocore.exceptions import ClientError

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Delete security group
try:
    # CHANGE
    response = ec2.delete_security_group(GroupId='sg-04fe0d799cc9dd1e2')
    print('Security Group Deleted')
except ClientError as e:
    print(e)