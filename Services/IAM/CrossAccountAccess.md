# Cross Account Access

## Objective

Praveen (root account - trusting account) wants to give an sam (IAM User) in Aamir (root account - trusted account) permissions for S3-ReadOnly in Praveen (root account). **Note that this exercise will require two AWS Accounts.**

1. Create an IAM User `sam` in Aamir (root account) with AWS Management Console Access and no other permissions. Specify the password and uncheck 'Require password reset'. Note down the URL this user has to login as.

1. In the Praveen (root account) create an IAM Role.
	- Select 'Another AWS Account'
	- Enter the Account ID of Aamir (root account).
	- Attach the AmazonS3ReadOnlyAccess Policy.
	- Give the role a 'sts-s3-read-only-role' name.
	- Expand the role and click on 'Trust relationships'.
	- Ckick on 'Edit trust relationship'.
	- Replace the arn with the arn of the IAM User created earlier.

1. In the Aamir (root account)
	- Expand the user
	- Click on 'Add inline policy'
	- Select STS as the service and AssumeRole as the Action
	- In the Resources click on 'Add ARN'
	- Paste the ARN of the Role created earlier.
	- Click on 'Review policy'
	- Give the policy 'sts-assume-role-policy' and click on 'Create policy'.

1. Try assuming the role
	- Login as the IAM user.
	- Click on the name on the top right
	- Select 'Switch Role'.
	- Click on 'Switch Role'.
	- Enter the Praveen (root account) account it and the role name.
	- Click on 'Switch Role'.
	- On the top right the user name should change.
	- Go to the S3 Management Console and the buckets in the Praveen (root account) should be visible for RO.

1. Clean the AWS Resources created earlier.

# Further Reading

1. Cross Account Access
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html