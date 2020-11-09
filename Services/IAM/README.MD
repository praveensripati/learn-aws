# Identity and Access Management

# Further Reading

1. Define permissions to access AWS resources based on tags
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html

1. AWS Networking, Environments and you (different approaches for isolating applications)
	- https://charity.wtf/2016/03/23/aws-networking-environments-and-you/

1. AWS Services That Work with IAM
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html

1. EC2 Error messages decoding
	- https://aws.amazon.com/blogs/security/demystifying-ec2-resource-level-permissions/
	- https://www.thecloudavenue.com/2019/07/how-to-use-tags-in-aws-to-give-resource.html

1. Policy Simulator
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html

1. What policies are required for MFA?
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage.html

1. What is ARN?
	- http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html

1. What is AWS Account Identifier?
	- http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html

1. Refining Permissions Using Service Last Accessed Data
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html
	- https://aws.amazon.com/blogs/security/automate-analyzing-permissions-using-iam-access-advisor/

1. Setup cross account access in AWS
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html

# All about writing IAM policies

1. An explicit deny statement takes precedence over allow statements.
	- http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow
	- Block everything by default
	- Deny takes precedence over Allow

1. IAM Policy Elements
	- http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html

1. Actions, Resources, and Condition Keys for AWS Services
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html

1. IAM JSON Policy Elements Reference
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html

1. Example policies
	- http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html

1. Restricting by tags
	- https://www.thecloudavenue.com/2019/07/how-to-use-tags-in-aws-to-give-resource.html
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html
	- http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_tag-owner.html
	- https://aws.amazon.com/premiumsupport/knowledge-center/iam-ec2-resource-tags/

1. IAM Policy condition based on time
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws-dates.html
	- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html

# TODO

1. Write a brief on the IAM Module.