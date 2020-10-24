# Installing Python SDK

1. Create an Ubuntu 18.04 t2.micro EC2 instance and connect to it.

1. Execute the below commands on the EC2 instance.
    >#become root\
    >sudo su

    >#Get the list of softwares\
    >apt-get update

    >#Install Python and pip\
    >apt-get install python2.7 python-pip -y

    >#Install Python AWS SDK\
    >pip install boto3

    >#Configure the SDK\
    >exit\
    >mkdir .aws\
    >echo -e "[default]\nregion=us-east-1" > .aws/config

# Further Reading

1. Quick start guide
    - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

1. Boto3 API
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html

1. Examples
    - https://github.com/awsdocs/aws-doc-sdk-examples
    - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/examples.html
    - https://github.com/aws-samples/

1. EC2 examples
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-ec2-create_instance.py.html
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-ec2-create_security_group.py.html
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-ec2-create_keypair.py.html

1. S3 examples
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-s3-s3-python-example-create-bucket.py.html
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-s3-put_object.py.html
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-s3-list_objects.py.html

1. SNS examples
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-sns-sns-python-example-create-topic.py.html
    - https://docs.aws.amazon.com/code-samples/latest/catalog/python-sns-sns-python-example-publish-to-topic.py.html