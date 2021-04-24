# Prerequisites to get started with EKS and ECS

1. Create an Ubuntu EC2 and connect to it.

1. Install the AWS CLI.

1. Navigate to the IAM Management Console and the Users Tab.

1. Click on `Add user`.

1. Give the user a name and select `Programmatic access`.

1. Click on `Next : Permissions`.

1. Select `Attach existing policies directly`.

1. Select `AdministratorAccess` under the policies.

1. Click on next twice.

1. Click on `Create user` and note down the `Access key ID` and `Secret access key`.

1. Provide the above access keys to the EC2 using the `aws configure` command along with the region `us-east-1`.

1. Install `eksctl`.
    >curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp\
    >sudo mv /tmp/eksctl /usr/local/bin\
    >eksctl version

1. Install `kubectl`.
    >curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.18.9/2020-11-02/bin/linux/amd64/kubectl  
    >chmod +x ./kubectl\
    >sudo mv ./kubectl /usr/local/bin\
    >kubectl version --short --client

1. Generate the ssh keys.
    >ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa