import boto3

if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')

    response = table.put_item(
        Item={
            'userid': 123,
            'name': "Praveen Sripati",
            'city': "Hyderabad",
            'country': "India"
        }
    )
    print("Put user succeeded:")
