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

select distinct(userIdentity.userName) from cloudtrail_logs_my_aws_cloudtrail_logs;

select count(*) from cloudtrail_logs_my_aws_cloudtrail_logs;

select distinct(userIdentity.userName) from cloudtrail_logs_my_aws_cloudtrail_logs;

select distinct(eventName) from cloudtrail_logs_my_aws_cloudtrail_logs where userIdentity.userName like 'devuser%';

select count(*) from cloudtrail_logs_my_aws_cloudtrail_logs where userIdentity.userName like 'devuser%' and eventName = 'RunInstances' and eventTime > '2020-10-01T00:00:00Z' and eventtime < '2020-10-31T23:59:59Z';

select count(*) from cloudtrail_logs_my_aws_cloudtrail_logs where userIdentity.userName like 'devuser%' and eventName = 'CreateDBInstance' and eventTime > '2020-10-01T00:00:00Z' and eventtime < '2020-10-31T23:59:59Z';