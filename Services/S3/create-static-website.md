1. Create a bucket and click on the bucket name.

1. Click on the Permissions tab. Click on `Block public access`. Click on Edit. Uncheck "Block all public access" and click on save.

1. Click on `Bucket Policy` and add the below policy in the `Bucket policy editor`. Make sure to change the bucket name with the bucket name created earlier. Click on Save. This allows public to get the objects in the bucket.

    ```
    {
    "Version":"2012-10-17",
    "Statement":[{
        "Sid":"PublicReadGetObject",
            "Effect":"Allow",
            "Principal": "*",
            "Action":["s3:GetObject"],
            "Resource":["arn:aws:s3:::praveen-web-site/*"
        ]
        }
    ]
    }
    ```

1. Click on Properties tab. Click on `Static website hosting`. Select `Use this bucket to host a website`. Enter the index document as index.html, error document as error.html. Make sure to note down the Endpoint. Click on Save.

1. Click on overview tab and click on Upload. Click on `Add files`. Upload the index.html and error.html files into the bucket.

1. Access the static website via the endpoint. Try to access a webpage which is not there and notice the error.html getting displayed.

# Further Reading

https://docs.aws.amazon.com/AmazonS3/latest/dev/HostingWebsiteOnS3Setup.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-actions-as-permissions
