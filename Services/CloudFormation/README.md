# Automation using the CloudFormation

CloudFormation Templates allow automation of the resource management in AWS. CloudFormation is similar to Ansible, Terraform and other. The only differentiation is that CloudFormation is very specific to AWS.

1. ec2-sg.creation.json and ec2-sg.creation.yaml create a Security Group when a stack is created out of it.

2. ec2-sg-creation.json and ec2-sg-creation.yaml creates an EC2 instance, a Security Group and connects both of them.

More complicated CloudFormation sample templates can be found in the AWS documentation [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html).

High level steps for CloudFormation
	- Add and connect resources
	- Add template parameters, mapping and outputs
	- Specify resource properties
	- Provision resources

# Further Reading

AWS CloudFormation\
https://aws.amazon.com/cloudformation/

Comparing CloudFormation with other similar tools\
https://cloudonaut.io/cloudformation-vs-terraform/
https://ryaneschinger.com/blog/aws-cloudformation-vs-terraform/

List of AWS Resources Supported\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html

Template anatomy\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html

Sample CloudFormation Templates\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html
https://github.com/widdix/aws-cf-templates
https://github.com/cfn-modules/docs

Walkthroughs\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_Using.html

Rollback on failure\
https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-prevent-rollback-failure/

Nested stacks (for reusability)\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html

Change Sets (previewing the changes when updating a Stack)\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

Detect drift on an entire CloudFormation stack\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html

Bringing existing resources into CloudFormation management\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html

AWS resource and property types reference\
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

Linter\
https://github.com/aws-cloudformation/cfn-python-lint