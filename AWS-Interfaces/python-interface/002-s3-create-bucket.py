import boto3

s3 = boto3.client('s3', region_name='us-east-1')

# CHANGE
s3.create_bucket(Bucket='my-bucket-praveen')