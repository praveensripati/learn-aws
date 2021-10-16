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

1. CloudFormation Workshop
	- https://cfn101.workshop.aws/

1. AWS CloudFormation best practices
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html

1. Quickly Retry Stack Operations from the Point of Failure
	- https://aws.amazon.com/blogs/aws/new-for-aws-cloudformation-quickly-retry-stack-operations-from-the-point-of-failure/

1. Exporting stack output values
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html

1. Introducing AWS CloudFormation Guard 2.0
	- https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-guard-2-0/

1. Handling Region parity with infrastructure as code
	- https://aws.amazon.com/blogs/mt/handling-region-parity-with-infrastructure-as-code/

1. Using AWS CloudFormation macros to perform custom processing on templates
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html

1. Comparing CloudFormation with other similar tools
	- https://cloudonaut.io/cloudformation-vs-terraform/
	- https://ryaneschinger.com/blog/aws-cloudformation-vs-terraform/
	- https://www.thecloudavenue.com/2020/09/aws-infrastructure-provisioning-with-ansible.html

1. AWS resource and property types reference
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

1. Template anatomy
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html

1. Sample CloudFormation Templates
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-services-us-east-1.html
	- https://cloudonaut.io/getting-started-with-aws-cf-templates/
	- https://github.com/cfn-modules/docs

1. Walkthroughs for auto generating the Template code 
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_Using.html

1. Rollback on failure
	- https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-prevent-rollback-failure/

1. Nested stacks (for reusability)
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html

1. Change Sets (previewing the changes when updating a Stack)
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

1. Detect drift on an entire CloudFormation stack
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html

1. Bringing existing resources into CloudFormation management
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html

1. Linter
	- https://github.com/aws-cloudformation/cfn-python-lint

1. CloudFormation Registry
	- https://aws.amazon.com/blogs/aws/introducing-a-public-registry-for-aws-cloudformation/
	- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html

1. Accelerate infrastructure as code development with open source Former2
	- https://aws.amazon.com/blogs/opensource/accelerate-infrastructure-as-code-development-with-open-source-former2/