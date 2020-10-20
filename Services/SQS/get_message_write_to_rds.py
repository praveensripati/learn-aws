import time
import boto3
import mysql.connector

queue_url = 'https://sqs.us-east-1.amazonaws.com/304000509264/CustomerQueue'

# Specify the database details
host = 'customerdb.cmeeo0ikklen.us-east-1.rds.amazonaws.com'
user = 'praveen'
password = 'praveen123'
database = 'customer_db'

# Create a SQS Client
sqs = boto3.client('sqs')

# Connect to the RDS MySQL Instance
mydb = mysql.connector.connect(
    host=host, user=user, password=password, database=database)
mycursor = mydb.cursor()

# Receive message from SQS queue
response = sqs.receive_message(QueueUrl=queue_url)
message = response['Messages'][0]

# Delete received message from queue
receipt_handle = message['ReceiptHandle']

sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

print('Received and deleted message: %s' % message["Body"])

# Get the customer name and address from the message
customerDetails = message["Body"]
customerDetailsList = customerDetails.split(',')
name = customerDetailsList[0]
address = customerDetailsList[1]

# Write the record to the database
val = (name, address)
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

mycursor.execute(sql, val)
mydb.commit()
print("Record inserted in the DB")
