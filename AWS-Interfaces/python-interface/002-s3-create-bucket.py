import boto3

s3 = boto3.client('s3', region_name='us-east-2')
location = {'LocationConstraint': 'us-east-2'}

# CHANGE
s3.create_bucket(Bucket='my-bucket-praveen', CreateBucketConfiguration=location)