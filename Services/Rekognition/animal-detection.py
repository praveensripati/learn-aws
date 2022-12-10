import boto3

# put the image in S3 and change the image_name below
image_name = "panda.jpg"

# get the labels for the image by calling DetectLabels from Rekognition
boto3 = boto3.Session()
client = boto3.client('rekognition', region_name="us-east-1")
response = client.detect_labels(Image={'S3Object': {'Bucket': "psripati-animals", 'Name': image_name}}, MaxLabels=10)
full_labels = response['Labels']

print('Detected labels for ' + image_name)
print('Labels = ' + str(full_labels))