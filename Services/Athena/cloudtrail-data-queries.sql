/*
Make sure the CloudTrial Trials is enabled
to write all the events to S3
*/

/*
Create a table in Athena ontime and map to the data in S3
Make sure to change the location of the S3 data
*/

CREATE EXTERNAL TABLE cloudtrail_logs_my_aws_cloudtrail_logs (
    eventVersion STRING,
    userIdentity STRUCT<
        type: STRING,
        principalId: STRING,
        arn: STRING,
        accountId: STRING,
        invokedBy: STRING,
        accessKeyId: STRING,
        userName: STRING,
        sessionContext: STRUCT<
            attributes: STRUCT<
                mfaAuthenticated: STRING,
                creationDate: STRING>,
            sessionIssuer: STRUCT<
                type: STRING,
                principalId: STRING,
                arn: STRING,
                accountId: STRING,
                userName: STRING>>>,
    eventTime STRING,
    eventSource STRING,
    eventName STRING,
    awsRegion STRING,
    sourceIpAddress STRING,
    userAgent STRING,
    errorCode STRING,
    errorMessage STRING,
    requestParameters STRING,
    responseElements STRING,
    additionalEventData STRING,
    requestId STRING,
    eventId STRING,
    resources ARRAY<STRUCT<
        arn: STRING,
        accountId: STRING,
        type: STRING>>,
    eventType STRING,
    apiVersion STRING,
    readOnly STRING,
    recipientAccountId STRING,
    serviceEventDetails STRING,
    sharedEventID STRING,
    vpcEndpointId STRING
)
COMMENT 'CloudTrail table for my-aws-cloudtrail-logs bucket'
ROW FORMAT SERDE 'com.amazon.emr.hive.serde.CloudTrailSerde'
STORED AS INPUTFORMAT 'com.amazon.emr.cloudtrail.CloudTrailInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://my-aws-cloudtrail-logs/AWSLogs/304000509264/CloudTrail/'
TBLPROPERTIES ('classification'='cloudtrail');

/*
Get the distinct users whose activities have been logged.
*/
select distinct(userIdentity.userName) from cloudtrail_logs_my_aws_cloudtrail_logs;

/*
Get the distinct activities performed by a user for any anamolies
*/
select distinct(eventName) from cloudtrail_logs_my_aws_cloudtrail_logs where userIdentity.userName like 'devuser%';

/*
Get the number of activites performed by a user between a certain start and end time
*/
select count(*) from cloudtrail_logs_my_aws_cloudtrail_logs where userIdentity.userName like 'devuser%' and eventName = 'RunInstances' and eventTime > '2020-10-01T00:00:00Z' and eventtime < '2020-10-31T23:59:59Z'