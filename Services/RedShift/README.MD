# Analytics with RedShift

1. Create a IAM role with AmazonS3ReadOnlyAccess policy for RedShift.

1. Go to the RedShift Management Console and create a cluster with the below details.
    - Free trial
    - Specify the database name, user name, password and note down the same
    - Under the Cluster permissions make sure to select the IAM Role created earlier
    - Click on `Create cluster`

1. Go to Query Editor in the RedShift Console
    - Specify the db name, username and password and connect to the cluster
    - Select the public schema

1. Go to Query Editor in the RedShift Console and execute the queries in the queries.sql to
    - Create the table
    - Load the data into it (the data is provided by AWS via S3)
    - Run queries on the table to do analytics

1. More complex queries can be found in the below URL.
    - https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html

1. Make sure to terminate the RedShift cluster.

# Further Reading

1. Data warehouse system architecture
    - https://docs.aws.amazon.com/redshift/latest/dg/c_high_level_system_architecture.html

1. Pricing
    - https://aws.amazon.com/redshift/pricing/

1. Getting Started with RedShift
    - https://aws.amazon.com/redshift/getting-started/
    - https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html

1. Getting Started with RedShift Spectrum
    - https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html

1. Athena uses Presto (https://prestosql.io/), RedShift uses PostgeSQL.
    - https://blog.openbridge.com/how-is-aws-redshift-spectrum-different-than-aws-athena-9baa2566034b
    - https://stackoverflow.com/questions/50250114/athena-vs-redshift-spectrum

1. COPY Examples from different sources
    - https://docs.aws.amazon.com/redshift/latest/dg/using-redshift-with-other-services.html
    - https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html

1. Building a Proof of Concept for Amazon Redshift
    - https://docs.aws.amazon.com/redshift/latest/dg/proof-of-concept-playbook.html

1. Uses cases
    - https://aws.amazon.com/redshift/customer-success/
    - https://aws.amazon.com/quicksight/customers/

1. BI Tools working with RedShift
    - https://aws.amazon.com/redshift/partners/
    - https://aws.amazon.com/quicksight/
    - https://aws.amazon.com/blogs/big-data/integrate-power-bi-with-amazon-redshift-for-insights-and-analytics/

1. ODBC and JDBC with RedShift
    - https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html
    - https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html

1. ETL into RedShift
    - https://aws.amazon.com/glue/
    - https://aws.amazon.com/datapipeline/

# TODO