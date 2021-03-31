# Accessing via HTTP in a language agnostic way

Requests can be made via SDK, CLI, but can also be done using the HTTP/HTTPS API Requests. This makes the AWS interface language agnostic, but is a bit low level. The HTTP/HTTPS API Requests requires that the request be signed, using the AccessKeys.

# Further Reading

1. Signing AWS requests with Signature Version 4
    - https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html

1. Signature Version 4 signing process
    - https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

1. Signature Version 2 signing process
    - https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html

1. Examples of the complete Signature Version 4 signing process (Python) - EC2, DynamoDB, IAM
    - https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html

1. EC2 Making API Requests
    - https://docs.aws.amazon.com/AWSEC2/latest/APIReference/making-api-requests.html
