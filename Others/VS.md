# Comparing different concepts around cloud.

It's easy to get confused :) Here I try to compare concepts related to the cloud.

1. Migrating from Lambda@Edge to CloudFront Functions
    - https://dev.to/aws-builders/migrating-from-lambda-edge-to-cloudfront-functions-3k7k

1. Kinesis vs. Kafka: Which Stream Processor Comes Out on Top?
    - https://www.lastweekinaws.com/blog/kinesis-vs-kafka-which-stream-processor-comes-out-on-top/

1. Aurora vs RDS
    - https://www.lastweekinaws.com/blog/aurora-vs-rds-an-engineers-guide-to-choosing-a-database/

1. Amazon ECS vs Amazon EKS: making sense of AWS container services
    - https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/

1. A comparison of EventBridge & Other AWS Services
    - https://www.rajeshbhojwani.co.in/2019/12/a-comparison-of-eventbridge-other-aws.html

1. EBS vs EFS vs S3
    - https://www.missioncloud.com/blog/resource-amazon-ebs-vs-efs-vs-s3-picking-the-best-aws-storage-option-for-your-business
    - https://dzone.com/articles/confused-by-aws-storage-options-s3-ebs-amp-efs-explained
    - https://medium.com/awesome-cloud/aws-difference-between-efs-and-ebs-8c0d72a348ad
    - Cost (EFS > EBS > S3)

1. Security Groups vs NACL
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison

1. Route53 Choosing between alias and non-alias records
    - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html

1. When should I use AWS Glue vs. AWS Data Pipeline?

    >AWS Glue provides a managed ETL service that runs on a serverless Apache Spark environment. This allows you to focus on your ETL job and not worry about configuring and managing the underlying compute resources. AWS Glue takes a data first approach and allows you to focus on the data properties and data manipulation to transform the data to a form where you can derive business insights. It provides an integrated data catalog that makes metadata available for ETL as well as querying via Amazon Athena and Amazon Redshift Spectrum.

    >AWS Data Pipeline provides a managed orchestration service that gives you greater flexibility in terms of the execution environment, access and control over the compute resources that run your code, as well as the code itself that does data processing. AWS Data Pipeline launches compute resources in your account allowing you direct access to the Amazon EC2 instances or Amazon EMR clusters.

    >Furthermore, AWS Glue ETL jobs are Scala or Python based. If your use case requires you to use an engine other than Apache Spark or if you want to run a heterogeneous set of jobs that run on a variety of engines like Hive, Pig, etc., then AWS Data Pipeline would be a better choice.

1. Different types of ELB
    - https://aws.amazon.com/elasticloadbalancing/details/#compare
    - https://www.sumologic.com/aws/elb/aws-elastic-load-balancers-classic-vs-application/
    - https://medium.com/containers-on-aws/using-aws-application-load-balancer-and-network-load-balancer-with-ec2-container-service-d0cb0b1d5ae5

1. Comparing Memcached and Redis
   - https://aws.amazon.com/elasticache/redis-vs-memcached/
   - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html

1. Choosing a Rehost Migration Tool – CloudEndure or AWS SMS
	- https://aws.amazon.com/blogs/architecture/field-notes-choosing-a-rehost-migration-tool-cloudendure-or-aws-sms/

1. Should I Run my Containers on AWS Fargate, AWS Lambda, or Both?
    - https://aws.amazon.com/blogs/architecture/should-i-run-my-containers-on-aws-fargate-aws-lambda-or-both/