
# AWS FAQ

While talking to someone around AWS or while conducting trainings, some of the questions pop up again and again. This page is an attempt to consolidate all such questions. These FAQ are also very good for the sake of interviews.

1. Create and activate an AWS account
    - https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/

1. Connecting to Your Linux Instance if You Lose Your Private Key
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replacing-lost-key-pair.html

1. How to work with windows EC2?
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html

1. AWS Products and Services by Regions
    - https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/

1. EC2 Instance Types
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html

1. How to create a username/password for EC2?
    - http://stackoverflow.com/a/7696451/614157

1. How to export AMI to another region?
    - https://aws.amazon.com/premiumsupport/knowledge-center/copy-ami-region/

1. How to work with shared and dedicated EC2 instances?
    - https://aws.amazon.com/ec2/dedicated-hosts/getting-started/
    - https://aws.amazon.com/ec2/dedicated-hosts/faqs/

1. How to work with your own IP pool?
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html

1. How to extend a existing EBS for Windows and Linux?
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-modify-volume.html
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/recognize-expanded-volume-windows.html
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html

1. Using EBS Snapshot in some other regions
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html

1. What are the IP address for after creation of the EFS
    - https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-ip-addr.html

1. How is the Spot Instance termination is handled?
     - https://aws.amazon.com/about-aws/whats-new/2018/01/amazon-ec2-spot-two-minute-warning-is-now-available-via-amazon-cloudwatch-events/
    - https://aws.amazon.com/blogs/aws/new-ec2-spot-instance-termination-notices/

1. Application Load Balancers and Classic Load Balancers support X-Forwarded-For, X-Forwarded-Proto, and X-Forwarded-Port headers.
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html

1. Client IP and ELB Logs
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html

1. Add existing EC2 to the AutoScalingGroup?
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-instance-asg.html

1. How to do the IAM Federation?
    - https://aws.amazon.com/identity/federation/
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html

1. http to https redirection in ELB?
    - https://aws.amazon.com/about-aws/whats-new/2018/07/elastic-load-balancing-announces-support-for-redirects-and-fixed-responses-for-application-load-balancer/

1. Specific use cases for Private ELB?
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-internal-load-balancers.html

1. AutoScaling using Custom Metrics
    - https://medium.com/qbits/autoscaling-using-custom-metrics-5f977903bc45
    - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html

1. Where do we specify the termination policy?
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html

1. Giving cross account permissions for the AWS permission?
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html

1. Region Codes
    - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html

1. How to use multiple security credentials?
    - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

1. What if the mobile phone is lost for the MFA authentication?
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html

1. How to make it mandatory for IAM user to use MFA for login?
    https://forums.aws.amazon.com/thread.jspa?threadID=154971

1. How to use RSA device for MFA?
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_u2f.html

1. How to use Tags in AWS to give resource permissions?
    - https://www.thecloudavenue.com/2019/07/how-to-use-tags-in-aws-to-give-resource.html

1. Resource Groups
    - https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html

1. Can the life cycle policy be applied on a subset of bucket data?
    - https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-lifecycle.html

1. VPC Resize
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-resize

1. What is the least CIDR that we can use in AWS VPC?
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#VPC_Sizing

1. What comes free with Trusted Advisor?
    - https://aws.amazon.com/premiumsupport/technology/trusted-advisor/

1. How do I reset the master user password for my Amazon RDS DB instance?
    - https://aws.amazon.com/premiumsupport/knowledge-center/reset-master-user-password-rds/

1. Limitations for S3 LifeCycle Policies
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html

1. Mounting EFS by IP address
    - https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-ip-addr.html

1. EC2 accidental termination
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination

1. Does ELB works as forward or reverse proxy? Mainly used for load balancing, but can also be used for reverse proxy.
    - https://smartproxy.com/blog/the-difference-between-a-reverse-proxy-and-a-forward-proxy
    - https://www.sumologic.com/blog/aws-elb-vs-nginx-load-balancer/
    - https://www.trianz.com/insights/reverse-proxying-requests-with-aws-elb-edge
    - https://www.nginx.com/resources/glossary/reverse-proxy-vs-load-balancer/

1. How to configure SSL in ELB?
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html

1. Weighted ELB?
    - https://aws.amazon.com/blogs/aws/new-application-load-balancer-simplifies-deployment-with-weighted-target-groups/

1. EFS access around multiple multiple regions and VPC
    - https://aws.amazon.com/about-aws/whats-new/2018/10/amazon-efs-now-supports-aws-vpn-and-inter-region-vpc-peering/
    - https://docs.aws.amazon.com/efs/latest/ug/efs-different-vpc.html

1. How to create an custom AMI in AWS?
    - https://kognitio.com/blog/making-amazon-machine-image/
    - http://work.haufegroup.io/automate-ami-with-packer/
    - https://www.elastic.co/blog/create-an-ami-from-your-own-vm-image

1. UI on Suse and RedHat
    - https://www.nomachine.com/accessing-your-remote-linux-desktop-on-amazon-elastic-compute-cloud-via-NoMachine
    - https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-2-install-gui/

1. General getting started with IT
    - Programming Language - https://www.tutorialspoint.com/python/index.htm
    - Database - https://www.tutorialspoint.com/mysql/index.htm
    - Linux - https://www.tutorialspoint.com/unix/index.htm

1. EndPoints
    - Interface VPC Endpoints (AWS PrivateLink) - https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html
    - Gateway VPC Endpoints - https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html
    - AWS New York Summit 2018 - AWS PrivateLink: Fundamentals (SRV211) - AWS New York Summit 2018 - AWS PrivateLink: Fundamentals (SRV211)

1. Limits of the ELB
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html

1. AWS CLI V1 vs V2
    - https://www.youtube.com/watch?v=U5y7JI_mHk8

1. What is master key in KMS?
    - Nothing more than a master key.

1. How to replace CMK Key for EBS Volumes? Without recreating the volumes.
     - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html

1. Can we change the rotation duration for AWS Managed Keys? Depends on the type of key as mentioned in the below document.
    - https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html

1. What is Envelope Encryption?
    - https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html

1. Rotating Customer Master Keys
    - https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html

1. What is master key in KMS?
    - https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html

1. How many versions can store in S3?
    - https://docs.amazonaws.cn/en_us/AmazonS3/latest/dev/list-obj-version-enabled-bucket.html

1. Getting started with storage gateway
    - https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStarted.html

1. What is Job Function in Policies
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html

1. How to use Tags in AWS to give resource permissions?
    - https://www.thecloudavenue.com/2019/07/how-to-use-tags-in-aws-to-give-resource.html

1. Can we restrict access keys to a specific IP?
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.html

1. Can Aurora DB have multiple writer nodes?
    - https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-multi-master.html

1. SNS Success/Failure Handling
    - https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html
    - https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-failed-sns-deliveries/

1. In what steps will AWS RDS increase the auto scaling for storage
    - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling

1. How to connect from Mac and Linux to Windows using RDP?
    - https://www.digitalcitizen.life/connecting-windows-remote-desktop-ubuntu
    - https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac

1. How to attach EBS to Windows EC2?
    - https://aws.amazon.com/premiumsupport/knowledge-center/attach-ebs-running-windows/

1. How to mount EFS to EC2 for cross region?
    - https://aws.amazon.com/about-aws/whats-new/2018/10/amazon-efs-now-supports-aws-vpn-and-inter-region-vpc-peering/
    - https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-vpc-peering.html

1. How many EBS can be attached to EC2?
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html

1. Selling RI in MarketPlace
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html

1. ALB Algorithm
    - https://aws.amazon.com/about-aws/whats-new/2019/11/application-load-balancer-now-supports-least-outstanding-requests-algorithm-for-load-balancing-requests/
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html
    - https://aws.amazon.com/blogs/aws/new-application-load-balancer-simplifies-deployment-with-weighted-target-groups/

1. Data Transfer Pricing
    - https://www.apptio.com/emerge/aws-data-transfer-costs/
    - https://aws.amazon.com/ec2/pricing/on-demand/

1. How to auto increment in DynamoDB?
    - https://stackoverflow.com/a/45899308/614157
    - https://martinstapel.com/how-to-autoincrement-in-dynamo-db-if-you-really-need-to/
    - https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.ConditionalUpdate

1. What is Projected using the Query operation?
    - https://www.tutorialspoint.com/dynamodb/dynamodb_global_secondary_indexes.htm

1. NAT Instance vs Gateway
    - https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html

1. AWS Public IP Range
    - https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html

1. How to join Linux EC2 in Microsoft Active Directory?
    - https://www.centrify.com/express/server-suite-form/

1. How do I use an MFA token to authenticate access to my AWS resources through the AWS CLI?
    - https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/

1. Configure SSL/TLS on Amazon Linux 2
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2.html

1. Cloud Patterns
    - https://docs.microsoft.com/en-us/azure/architecture/patterns/

1. How can I utilize user data to automatically execute a script with every restart of my Amazon EC2 instance?
    - https://aws.amazon.com/premiumsupport/knowledge-center/execute-user-data-ec2/

1. Create a PEM from a PPK file
    - https://stackoverflow.com/questions/33273180/create-a-pem-from-a-ppk-file

1. S3 Demo around Tagging
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-configuration-examples.html#lifecycle-config-ex1

1. S3 Detection for Malware/Virus
    - S3 has no feature for the same, it has to be integrated with AWS Macie.
    - https://docs.aws.amazon.com/macie/latest/userguide/what-is-macie.html
    - https://docs.aws.amazon.com/macie/latest/userguide/macie-alerts.html

1. Supported S3 transitions and related constraints
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html

1. Snow device pricing
    - https://aws.amazon.com/snowcone/pricing/
    - https://aws.amazon.com/snowball/pricing/
    - https://aws.amazon.com/snowmobile/pricing/

1. S3 Multi Part Upload
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html

1. Route53 Routing policy
    - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

1. Attach a root EBS Volume to a new EC2
    - https://www.youtube.com/watch?v=C6lSCAVggFE
    - https://stackoverflow.com/questions/6377669/can-i-change-the-root-ebs-device-of-my-amazon-ec2-instance

1. EBS Mirroring can be done using RAID
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/raid-config.html
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/raid-config.html

1. Youtube - ALB
    - https://www.youtube.com/watch?v=sNcKYcFKOB4

1. Creating Network Load Balancer
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-getting-started.html

1. What is CORS?
    - https://www.codecademy.com/articles/what-is-cors
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    - http://restlet.com/company/blog/2015/12/15/understanding-and-using-cors/

1. CORS in AWS
    - https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-cors-configuration.html
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html

1. How to integrate LDAP with IAM?
    - https://aws.amazon.com/blogs/security/aws-federated-authentication-with-active-directory-federation-services-ad-fs/
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html

1. Info on how to create a HA RDS
    - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
    - https://aws.amazon.com/blogs/database/amazon-rds-under-the-hood-multi-az/
    - https://www.youtube.com/watch?v=uiiS1h4PSI8

1. What is Cloud Native?
    - https://www.redhat.com/en/topics/cloud-native-apps

    >Cloud-native applications are a collection of small, independent, and loosely coupled services. They are designed to deliver well recognized business value, like the ability to rapidly incorporate user feedback for continuous improvement. In short, cloud-native app development is a way to speed up how you build new applications, optimize existing ones, and connect them all together. Its goal is to deliver apps users want at the pace a business needs.

1. Different ways of connecting the on-premise network to the AWS network
     - https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html

1. Replacing Auto Scaling instances based on an instance refresh
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html

1. How can I automate Amazon EBS snapshot management using Amazon Data Lifecycle Manager?
    - https://aws.amazon.com/premiumsupport/knowledge-center/ebs-snapshot-data-lifecycle-manager/

1. Difference between LogGroup and LogStream in CloudWatch Logs
    - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html

1. Lambda functions as targets for Application ELB
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html

1. Use RSA private key to generate public key?
    - https://stackoverflow.com/a/5246045/614157

1. Attaching a volume to multiple instances with Amazon EBS Multi-Attach
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html

1. How do I set up weighted target groups for my Application Load Balancer?
    - https://aws.amazon.com/premiumsupport/knowledge-center/elb-make-weighted-target-groups-for-alb/

# TODO

1. Categorize the questions based on services. Makes it easy to find the appropriate question.

2. May be use tags for categorizing the FAQ.

3. Delete the duplicates (use shell commands)