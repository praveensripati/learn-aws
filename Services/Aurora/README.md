# Topics

    - What is Aurora and different features of Aurora?
    - How is Aurora different from the RDBMS?
    - Optimization techniques in Aurora. (???)
    - Creating an Aurora DB along with exploring the different features.

## Theory

### General

1. Amazon Aurora doesn't fall under the free tier.

1. Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud.

1. Amazon Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases.

1. It provides the security, availability, and reliability of commercial databases at 1/10th the cost.

### High Availability

1. Amazon Aurora is designed to offer greater than 99.99% availability, replicating 6 copies of your data across 3 Availability Zones and backing up your data continuously to Amazon S3. The price is built into the Aurora pricing. Amazon Aurora automatically divides your database volume into 10GB segments spread across many disks.

1. Amazon Aurora supports up to 15 replicas within the same region. Promoting one of the replica as the new primary takes about 30 seconds. During which the application can be done. The flipping is done by changing the CNAME records.

1. Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions. It supports up to five secondary AWS regions. Each of the region can have 15 Aurora Replicas.

1. If your primary region becomes unavailable, you can manually remove a secondary region from an Aurora Global Database and promote it to take full reads and writes. You will also need to point your application to the newly promoted region.

1. Amazon Aurora Multi-Master is a new feature of the Aurora MySQL-compatible edition that adds the ability to scale out write performance across multiple Availability Zones, allowing applications to direct read/write workloads to multiple instances in a database cluster and operate with continuous availability (not higher availability).

### Scaling

1. Storage can be between 10GB to 128GB in 10GB increments.

1. Changing the instance type for Aurora RDS can lead to downtime and so is Serverless.

1. Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas provisioned for an Aurora DB cluster using single-master replication.

1. An Aurora Serverless DB cluster automatically starts up, shuts down, and scales capacity up or down based on your application's needs. Aurora Serverless provides a relatively simple, cost-effective option for infrequent, intermittent, or unpredictable workloads. Pricing is based on Aurora Capacity Units (ACUs).

### Migration

1. To migrate from commercial database engines, you can use the AWS Database Migration Service for a secure migration with minimal downtime.

1. The native import/export utilities can also be used for the Migration.

1. Create a Read Replica and promote it.

### Backups

1. Automated backups are always enabled on Amazon Aurora DB Instances. 

1. With Amazon Aurora with MySQL compatibility, you can backtrack a DB cluster to a specific time, without restoring data from a backup.

1. You can restore a DB cluster to a specific point in time, creating a new DB cluster.

## Optimization

1. Build applications to drive a large number of concurrent queries and transactions.

1. Amazon Aurora Parallel Query refers to the ability to push down and distribute the computational load of a single query across thousands of CPUs in Aurora’s storage layer. Without Parallel Query, a query issued against an Amazon Aurora database would be executed wholly within one instance of the database cluster; this would be similar to how most databases operate.

## Further Reading

1. Amazon Aurora ascendant: How we designed a cloud-native relational database
    - https://www.allthingsdistributed.com/2019/03/Amazon-Aurora-design-cloud-native-relational-database.html

1. Getting started with Amazon Aurora
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.html

1. Aurora Pricing
    - https://aws.amazon.com/rds/aurora/pricing/

1. Aurora FAQ
    - https://aws.amazon.com/rds/aurora/faqs/

1. Aurora Global Database
    - https://aws.amazon.com/rds/aurora/global-database/

1. Aurora Serverless
    - https://aws.amazon.com/rds/aurora/serverless/

1. Working with Aurora multi-master clusters
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-multi-master.html

1. Amazon Aurora Parallel Query
    - https://aws.amazon.com/rds/aurora/parallel-query/

1. Testing Amazon Aurora using fault injection queries
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.FaultInjectionQueries.html

1. Altering tables in Amazon Aurora using fast DDL
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.FastDDL.html

1. Integrating Amazon Aurora MySQL with other AWS services
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.html

1. Using Amazon Aurora Auto Scaling with Aurora replicas
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html

1. Backtracking an Aurora DB cluster
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html

1. Restoring a DB cluster to a specified time
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PIT.html

1. Best practices with Amazon Aurora
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html

1. Managing performance and scaling for Aurora DB clusters
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html

1. Why is Aurora faster?
    - https://www.allthingsdistributed.com/2019/03/Amazon-Aurora-design-cloud-native-relational-database.html
    - https://www.percona.com/blog/2015/11/16/amazon-aurora-looking-deeper/
    - https://www.percona.com/blog/2018/07/17/when-should-i-use-amazon-aurora-and-when-should-i-use-rds-mysql/

1. Loading the data from S3 to Aurora
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.LoadFromS3.html