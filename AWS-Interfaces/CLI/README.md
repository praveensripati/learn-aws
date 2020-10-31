The AWS CLI can be installed on the EC2 and also on the non-EC2 (Laptop/Server etc). Both Windows and Linux OS are supported.

## AWS CLI for Windows

1. Download and install the AWS CLI as like any other software on Windows.
    - https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#install-msi-on-windows

1. Once the installation is done, confirm the same by running the `aws --version` command.

## AWS CLI for Ubuntu

1. Create an Ubuntu EC2 instance and execute the below commands.
    >sudo apt-get update\
    >sudo apt-get install python3 python3-pip -y\
    >pip3 install awscli --upgrade\
    >export PATH="$PATH:/home/ubuntu/.local/bin/"

    https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html

## For **non-EC2** instances

1. Generate the credentials from the [this](https://console.aws.amazon.com/iam/home?region=us-east-1#/security_credential) link.
    - Click on `Continue with Security Credentials`
    - Click on `Access keys (access key ID and secret access key)`.
    - Click on `Create New Access Key`.
    - Note down the keys.

1. Run the `aws configure` command to specify the region (us-east-1 for North Virginia) and the keys. For the default output format leave blank.

## For the **EC2** instances

1. Create an IAM Role with the AdministrativeAccess policy and attach the same to the EC2 instance.

1. Run the `aws configure` command to specify **only** the region (us-east-1 for North Virginia).

## Execute the below commands to interact with the AWS resources

1. Create the Security Group and open port 22.
    >aws ec2 create-security-group --group-name ssh-access --description "allow ssh"
    >aws ec2 authorize-security-group-ingress --group-name ssh-access --protocol tcp --port 22 --cidr 0.0.0.0/0

1. Get the subnets in the VPC
    >aws ec2 describe-subnets

1. Terminate the instance (make sure to replace the instance-ids with an existing one)
    >aws ec2 terminate-instances --instance-ids i-032154634c23e4868

1. Get more commands from the below CLI Reference Guide (v1) and try them out.

# Further Reading

1. CLI Reference Guide
    - https://docs.aws.amazon.com/cli/latest/reference/ (v1)
    - https://awscli.amazonaws.com/v2/documentation/api/latest/index.html (v2)

1. AWS CLI v1 vs v2
    - https://www.youtube.com/watch?v=U5y7JI_mHk8

1. Configure Auto Completion with the CLI
    - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-completion.html

1. s3 vs s3api commands
    - https://aws.amazon.com/blogs/developer/leveraging-the-s3-and-s3api-commands/