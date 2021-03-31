# Common commands to work with AWS faster

1. All objects without specifying a prefix.
    >aws s3 rm s3://praveen --recursive

1. Decode the authorization failure message.
    >aws sts decode-authorization-message --encoded-message (encoded error message) --query DecodedMessage --output text | jq '.'