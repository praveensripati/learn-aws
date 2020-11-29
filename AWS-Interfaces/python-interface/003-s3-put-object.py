import boto3

# Create an S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# CHANGE
# Also, create a file before uploading
filename = 'file.txt'
bucket_name = 'my-bucket-praveen'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)