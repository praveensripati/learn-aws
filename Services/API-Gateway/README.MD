# Service Name

With a few clicks in the AWS Management Console, you can create an API that acts as a “front door” for applications to access data, business logic, or functionality from your back-end services, such as applications running on Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Container Service (Amazon ECS) or AWS Elastic Beanstalk, code running on AWS Lambda, or any web application.

    - Metering
	- Security
	- Resiliency
	- Monitoring
	- LifeCycle Management
	- Rest and WebSockets API
	- Throttling

REST services take actions corresponding to the HTTP request verb. These four are meant to correspond to the CRUD model, with POST equating to Create, GET equating to Read, PUT equating to Update, and DELETE equating to Destroy.

    - HTTP POST -> Create
    - HTTP GET -> Read
    - HTTP PUT -> Update
    - HTTP DELETE -> Destroy

## REST Hierarchy

- API -> Resource -> HTTP METHOD -> Lambda
- Insurance -> Policy -> Create Method -> CreatePolicyLambda

## Steps to get started with the API Gateway Service

1. Create a Lambda execution role (lambda-apigateway-role) with the `lambda-permissions.json`. The policy gives the permissions to CloudWatch and DynamoDB.

1. Create a Lambda Function (LambdaFunctionOverHttps) with the `LambdaFunctionOverHttps.js` code. And also attach the role created earlier. The runtime should be Node.js 10x.

1. Create a table in DynamoDB with the following details.

    >Table name – lambda-apigateway\
    >Primary key – id (string)

1. Test the Lambda function using the below Payload. An item should be inserted in the DynamoDB. Delete the item from the DynamoDB.
    ```
    {
        "operation": "create",
        "tableName": "lambda-apigateway",
        "payload": {
            "Item": {
                "id": "1",
                "name": "Bob"
            }
        }
    }
    ```
1. Go to the API Gateway Service and create a new API (DynamoDBOperations).

1. Click on Actions and "Create Resourse". Enter the "Resource Name" as DynamoDBManager.

1. Click on Actions and "Create Method". Select "POST" and click on the Tick. In the LambdaFunction enter LambdaFunctionOverHttps. Click on Save. The permissions for the API Gateway to call the Lambda will be set automatically.

1. Under the Test, Click on the blaze button to test the API Gateway. In the Request Body enter the below payload. The test should complete with a status 200. And also the item should be inserted in the DynamoDB table. Also, in the Lambda monitoring the Invocations and the "Error count and success rate" should be reflected appropriately.
    ```
    {
        "operation": "create",
        "tableName": "lambda-apigateway",
        "payload": {
            "Item": {
                "id": "1",
                "name": "Bob"
            }
        }
    }
    ```
1. The API can be deployed in stages. Again click on Action -> Deploy API. Enter the "Stage name" as Prod. Click on Deploy. The "Invoke URL" is provided. External clients can make a REST call to the "Invoke URL" to call the Lambda function.

1. Use the below curl command to invoke the REST API. Note to change the URL at the end. Also, the same can be done programatically from any language also.

    >curl -X POST -d "{\"operation\":\"create\",\"tableName\":\"lambda-apigateway\",\"payload\":{\"Item\":{\"id\":\"1\",\"name\":\"Bob\"}}}" https://y6hfdzwgbi.execute-api.us-east-1.amazonaws.com/test-stage/dynamodbmanager

# Further Reading

1. Build a Serverless Web Application with AWS Lambda, Amazon API Gateway, Amazon S3, Amazon DynamoDB, and Amazon Cognito
    - https://aws.amazon.com/getting-started/projects/build-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/

1. Using AWS Lambda with Amazon API Gateway (Uses the AWS CLI)
    - https://docs.aws.amazon.com/lambda/latest/dg/with-on-demand-https-example.html

# TODO

1. Need to check if the Lambda code works with NodeJS 10x.