# Automation using the CloudFormation

CloudFormation Templates allow automation of the resource management in AWS. CloudFormation is similar to Ansible, Terraform and other. The only differentiation is that CloudFormation is very specific to AWS.

1. `ec2-sg.creation.json` and `ec2-sg.creation.yaml` create a Security Group when a stack is created out of it.

2. `ec2-sg-creation.json` and `ec2-sg-creation.yaml` creates an EC2 instance, a Security Group and connects both of them.

More complicated CloudFormation sample templates can be found in the AWS documentation [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html).

High level steps for CloudFormation
	- Add and connect resources
	- Add template parameters, mapping and outputs
	- Specify resource properties
	- Provision resources

# Further Reading

1. AWS CloudFormation
	- https://aws.amazon.com/cloudformation/

1. Comparing CloudFormation with other similar tools
	- https://cloudonaut.io/cloudformation-vs-terraform/
	- https://ryaneschinger.com/blog/aws-cloudformation-vs-terraform/
	- https://www.thecloudavenue.com/2020/09/aws-infrastructure-provisioning-with-ansible.html

1. List of AWS Resources Supported
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html

1. AWS resource and property types reference
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

1. Template anatomy
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html

1. Sample CloudFormation Templates
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-services-us-east-1.html
	- https://github.com/widdix/aws-cf-templates
	- https://github.com/cfn-modules/docs

1. Walkthroughs for auto generating the Template code 
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_Using.html

1. Rollback on failure
	- https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-prevent-rollback-failure/

1. Nested stacks (for reusability)
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html

1. Change Sets (previewing the changes when updating a Stack)
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

1. Detect drift on an entire CloudFormation stack
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html

1. Bringing existing resources into CloudFormation management
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html

1. Linter
	- https://github.com/aws-cloudformation/cfn-python-lint