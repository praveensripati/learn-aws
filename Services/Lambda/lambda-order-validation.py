def lambda_handler(event, context):

    if (len(event['CC']) == 16 and int(event['Price']) > 0):
        StatusCode = 1
    else:
    StatusCode = 0
    
    return {
        'Status': StatusCode,
        'OrderId': event['OrderId'],
        'Name': event['Name'],
        'ItemName': event['ItemName'],
        'Price': event['Price'],
        'CC': event['CC']
    }
