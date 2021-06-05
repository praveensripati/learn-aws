
1. IAM Policies and Bucket Policies and ACLs! Oh, My! (Controlling Access to S3 Resources)
    - https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/

1. Service control policy (SCP) vs IAM Policy
    - https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html

    A policy that specifies the services and actions that users and roles can use in the accounts that the SCP affects. SCPs are similar to IAM permissions policies except that they don't grant any permissions. Instead, SCPs specify the maximum permissions for an organization, organizational unit (OU), or account. When you attach an SCP to your organization root or an OU, the SCP limits permissions for entities in member accounts.

1. Identity-based policies and resource-based policies
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html