# Getting started with Lambda

[Serverless](https://aws.amazon.com/elasticache/) is a different mindset where we don't need to think about servers. Since, we don't need to think about servers, we don't need to worry about the below aspects. AWS will take care of them us and we can focus more on the business.

- Capacity Planning
- Scalability
- Availability
- Provisioning
- Reliability

SNS, SQS, SES, S3 along with Lambda are a few AWS Services which follow the serverless model. The bad thing about Lambda is the code is specific to the AWS and has to be ported/migrated before running it in some other Cloud. Knative allows to run functions in a Cloud agnostic way.

1. `lambda-nodejs-send-ses-email-s3trigger.js` is a JS code which uses AWS SES to send an email. This can be integrated with S3. So, when an object is uploaded to S3, it can automatically trigger the Lambda function which will send an email notification. Note that both the email addresses have to verified in the SES.

1. `lambda-nodejs-publish-sns-topic-sqs-trigger.js` again is a JS code which publishes a messaged to an SNS Topic. This Lambda function can be integrated with SQS. As soon as a messages is put in the Queue, it triggers the Lambda functions which publishes a messages to the SNS Topic.

# Further Reading

1. AWS Serverless
    - https://aws.amazon.com/serverless/

1. Differences between CloudFront Functions and Lambda@Edge
    - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html
    - https://dev.to/aws-builders/migrating-from-lambda-edge-to-cloudfront-functions-3k7k

1. How do I give internet access to a Lambda function that's connected to an Amazon VPC?
    - https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/

1. Configuring interface VPC endpoints for Lambda
    - https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-endpoints.html

1. Configuring a Lambda function to access resources in a VPC
    - https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html

1. AWS Lambda execution environment
    - https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html

1. Firecracker (VM technology for Fargate and Lambda) and BottleRocket (Container OS for K8S for customers)
    - https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/
    - https://aws.amazon.com/about-aws/whats-new/2018/11/firecracker-lightweight-virtualization-for-serverless-computing/
    - https://aws.amazon.com/bottlerocket/

1. Use AWS PrivateLink to Access AWS Lambda Over Private AWS Network
    - https://aws.amazon.com/blogs/aws/new-use-aws-privatelink-to-access-aws-lambda-over-private-aws-network/

1. Shrinking an S3 image with NodeJS\
    - https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html

1. Collation of articles on Serverless Architecture
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

1. Choosing between AWS Lambda data storage options in web apps
    - https://aws.amazon.com/blogs/compute/choosing-between-aws-lambda-data-storage-options-in-web-apps/

1. Auto generate the IAM policies for the Lambda (code is not updated much)
    - https://github.com/puresec/serverless-puresec-cli

1. Lambda functions as targets for Application ELB
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html

1. AWS Lambda Extensions
    - https://aws.amazon.com/lambda/aws-learning-path-lambda-extensions/
    - https://pages.awscloud.com/Integrating-AWS-Lambda-with-Your-Favorite-Tools_2021_0614-SRV_OD.html

1. Deploying Lambda using AWS Development Tools
    - https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam.html
    - https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-lambda.html
    - https://www.youtube.com/watch?v=aGI4Wlm5c9U

1. Lambda multiple invocations
    - https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html
    
    For asynchronous invocation, Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a dead-letter queue.

1. Comparing Lambda invocation modes
    - https://docs.aws.amazon.com/lambda/latest/operatorguide/invocation-modes.html