# Automation using the CloudFormation

CloudFormation Templates allow automation of the resource management in AWS. CloudFormation is similar to Ansible, Terraform and other. The only differentiation is that CloudFormation is very specific to AWS.

1. ec2-sg.creation.json and ec2-sg.creation.yaml create a Security Group when a stack is created out of it.

2. ec2-sg-creation.json and ec2-sg-creation.yaml creates an EC2 instance, a Security Group and connects both of them.

More complicated CloudFormation sample templates can be found in the AWS documentation [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html).

## Further Reading

https://aws.amazon.com/cloudformation/

