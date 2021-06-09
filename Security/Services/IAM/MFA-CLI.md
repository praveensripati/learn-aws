
Lets say that the AWS account credentials get compromised, the hacker should be able to access the account and do a lot of damage. This is where the [AWS MFA](https://aws.amazon.com/iam/features/mfa/) comes into play. But, the MFA doesn't apply the CLI/SDK operations by default and some additional work has to be done.

1. Create an IAM Policy with one of the the below JSON. Both have the same effect of giving the access to all the S3 operations using the short term access keys authenticated via the MFA.
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Action": "s3:*",
                "Resource": "*",
                "Condition": {
                    "BoolIfExists": {
                        "aws:MultiFactorAuthPresent": "false"
                    }
                }
            }
        ]
    }
    ```
    ```
    {
        "Version": "2012-10-17",
        "Id": "123",
        "Statement": [
            {
                "Effect": "Deny",
                "Resource": "*",
                "Action": "s3:*",
                "Condition": {
                    "Null": {
                        "aws:MultiFactorAuthAge": true
                    }
                }
            }
        ]
    }
    ```
1. Create an IAM User and get the access keys for this user.

1. Attach the above Policy and the AmazonS3FullAccess Policy to the IAM user.

1. Enable MFA for the user.

1. Install the AWS CLI.

1. Set the above access keys using the `aws configure` command. Specify the appropriate Region code.

1. Get the short term credentials for the same IAM User using the below command. Make sure to replace the arn-of-the-mfa-device and code-from-token in the command.

    >aws sts get-session-token --serial-number arn-of-the-mfa-device --token-code code-from-token

1. In the `.aws/credendtials` file create a named profile with the below content. Make sure to replace the access key, secret access key and the session token from the previous command.

    >[mfa]
    >aws_access_key_id = example-access-key-as-in-returned-output
    >aws_secret_access_key = example-secret-access-key-as-in-returned-output
    >aws_session_token = example-session-Token-as-in-returned-output

1. The below command uses the default named profile and so the long term credentials and so should fail.

    >aws s3 ls

1. The below command uses the long term credentials authenticated via MFA and should return the list of buckets in S3. 

    >aws s3 ls --profile mfa

# Further Reading

1. AWS CLI and MFA
	- https://stackoverflow.com/a/67886052/614157

1. How do I use an MFA token to authenticate access to my AWS resources through the AWS CLI?
    - https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/

1. How can I enforce MFA authentication for IAM users that use the AWS CLI?
    - https://aws.amazon.com/premiumsupport/knowledge-center/mfa-iam-user-aws-cli/

1. Adding a bucket policy to require MFA
    - https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-use-case-7

1. aws:MultiFactorAuthPresent
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-multifactorauthpresent

1. Boolean Condition
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_Boolean
	
1. IfExists condition
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_IfExists