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

# Further Reading

1. Home Page
    - https://aws.amazon.com/lambda/

1. AWS Serverless
    - https://aws.amazon.com/serverless/

1. Firecracker (VM technology for Fargate and Lambda) and BottleRocket (Container OS for K8S for customers)
    - https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/
    - https://aws.amazon.com/about-aws/whats-new/2018/11/firecracker-lightweight-virtualization-for-serverless-computing/
    - https://aws.amazon.com/bottlerocket/

1. Use AWS PrivateLink to Access AWS Lambda Over Private AWS Network
    - https://aws.amazon.com/blogs/aws/new-use-aws-privatelink-to-access-aws-lambda-over-private-aws-network/

1. Shrinking an S3 image with NodeJS\
    - https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html

1. Collation of articles on Serverless Architecture\
    - https://aws.amazon.com/blogs/architecture/ten-things-serverless-architects-should-know/

1. How to Design Your Serverless Apps for Massive Scale
    - https://aws.amazon.com/blogs/architecture/how-to-design-your-serverless-apps-for-massive-scale/

1. Bootstrapping a Java Lambda application with minimal AWS Java SDK startup time using Maven
    - https://aws.amazon.com/blogs/developer/bootstrapping-a-java-lambda-application-with-minimal-aws-java-sdk-startup-time-using-maven/

1. Lambda Concurrency
    - https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html
    - https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html

1. Replacing web server functionality with serverless services
    - https://aws.amazon.com/blogs/compute/replacing-web-server-functionality-with-serverless-services/
