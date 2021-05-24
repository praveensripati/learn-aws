#!/usr/bin/env python
import sys
import boto3

# total arguments
n = len(sys.argv)

s3 = boto3.resource('s3')

for i in range(1, n):

	print("Deleting bucket : " + sys.argv[i])
	bucket = s3.Bucket(sys.argv[i])

	# Delete all object versions in the bucket
	bucket.object_versions.delete()

	# Delete the bucket
	bucket.delete()