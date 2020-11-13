# Athena

Athena is a service to process the data in S3 using standard SQL queries. It's all serverless and there is no need to do any capacity planning. The pricing for Athena depends on the amount of data scanned in S3.

1. `airline-data-queries.sql` has the sequence of steps to process the Airline dataset provided Hardvard Dataverse. The same can be downloaded from [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7) and uploaded into S3 for further processing.

1. `cloudtrail-data-queries.sql` has the sequence of steps to process the CloudTrial Trials data which can be used for auditing the user or the application activities in AWS.

# Further Reading

1. Athena uses Presto (https://prestosql.io/), RedShift uses PostgeSQL.
    - https://blog.openbridge.com/how-is-aws-redshift-spectrum-different-than-aws-athena-9baa2566034b
    - https://stackoverflow.com/questions/50250114/athena-vs-redshift-spectrum

1. Athena Federated Query
    - https://aws.amazon.com/blogs/big-data/query-any-data-source-with-amazon-athenas-new-federated-query/

1. Redacting sensitive information with user-defined functions in Amazon Athena
    - https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/