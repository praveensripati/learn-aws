# Getting started with Lambda

[Serverless](https://aws.amazon.com/elasticache/) is a different mindset where we don't need to think about servers. Since, we don't need to think about servers, we don't need to worry about the below aspects. AWS will take care of them us and we can focus more on the business.

- Capacity Planning
- Scalability
- Availability
- Provisioning
- Reliability

SNS, SQS, SES, S3 along with Lambda are a few AWS Services which follow the serverless model. The bad thing about Lambda is the code is specific to the AWS and has to be ported/migrated before running it in some other Cloud. Knative allows to run functions in a Cloud agnostic way.

1. **lambda-nodejs-send-ses-email-s3trigger.js** is a JS code which uses AWS SES to send an email. This can be integrated with S3. So, when an object is uploaded to S3, it can automatically trigger the Lambda function which will send an email notification. Note that both the email addresses have to verified in the SES.

2. **lambda-nodejs-publish-sns-topic-sqs-trigger.js** again is a JS code which publishes a messaged to an SNS Topic. This Lambda function can be integrated with SQS. As soon as a messages is put in the Queue, it triggers the Lambda functions which publishes a messages to the SNS Topic.

## Further Reading

https://aws.amazon.com/lambda/