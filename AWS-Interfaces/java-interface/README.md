# Installing Java SDK

1. Create an Ubuntu 18.04 t2.micro EC2 instance and connect to it.

1. Execute the below commands to install maven and java-common.
    >sudo apt-get update\
    >sudo apt install maven java-common

1. Download the latest Corretto (Java SDK from Amazon) using the wget command.\
    >wget https://d3pxv6yz143wms.cloudfront.net/11.0.5.10.1/java-11-amazon-corretto-jdk_11.0.5.10-1_amd64.deb\
    >sudo dpkg --install java-11-amazon-corretto-jdk_11.0.5.10-1_amd64.deb

1. Create an IAM Role with AmazonS3FullAccess policy attached.
Attach the IAM Role to the EC2.

1. Create basic maven package
    >mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=org.example.basicapp -DartifactId=myapp
  
1. Delete the pom.xml in the myapp folder and replace with the one in this folder.

1. Execute the below commands on the EC2 instance. Make sure there are no errors.
    >cd /home/ubuntu/myapp/src/main/java/org/example/basicapp\
    >rm App.java\
    >Copy the code from java-aws-sdk-code/S3Sample.java\
    >cd ~/myapp\
    >mvn clean compile exec:java\

1. Note from the S3 Management Console that a bucket with the name starting with `my-first-s3-bucket-` will be created a file uploaded to it.

# Further Reading

1. AWS Java SDK
    - https://aws.amazon.com/developers/getting-started/java/
    - https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/getting-started.html

1. What is AWS tookit for Eclipse
    - https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/welcome.html
    - https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/setup-install.html
    - https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/setup-credentials.html

1. Run a AWS application in Eclipse
    - https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/tke_java_apps.html

1. Examples
    - https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services.html
    - https://github.com/aws/aws-sdk-java/tree/master/src/samples
    - https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-javav2.html