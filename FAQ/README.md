
# AWS FAQ

While talking to someone around AWS or while conducting trainings, some of the questions pop up again and again. This page is an attempt to consolidate all such questions. These FAQ are also very good for the sake of interviews.

## First Things First

1. Create and activate an AWS account
    - https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/
    - https://aws.amazon.com/premiumsupport/plans/

1. AWS Documentation
    - https://docs.aws.amazon.com/

1. AWS Documentation is Now Open Source and on GitHub
    - https://aws.amazon.com/blogs/aws/aws-documentation-is-now-open-source-and-on-github/

1. AWS Free tier
    - https://aws.amazon.com/free/
    - https://aws.amazon.com/blogs/aws/aws-free-tier-update-new-customers-can-get-started-and-explore-aws-with-up-to-200-in-credits/


1. AWS Infrastructure
    - https://aws.amazon.com/about-aws/global-infrastructure/
    - https://aws.amazon.com/cloudfront/features/

1. AWS Products and Services by Regions
    - https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/

1. Region Codes
    - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html

1. How do I convert a .pem file into a .ppk, and vice versa, on Windows and Linux?
    - https://aws.amazon.com/premiumsupport/knowledge-center/ec2-ppk-pem-conversion/

## Everything Else

1. Receiving email with Amazon SES
    - https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html

1. Why is CloudFront serving outdated content from Amazon S3?
    - https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serving-outdated-content-s3/

1. How many EC2's can be attached to a single EBS volume?
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html

1. Auto Scaling groups with multiple instance types and purchase options
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html

1. How do I attach a new EBS volume to a running Amazon EC2 Windows instance?
    - https://aws.amazon.com/premiumsupport/knowledge-center/attach-ebs-running-windows/

1. Why are S3 and Google Storage bucket names a global namespace?
    - https://stackoverflow.com/questions/24112647/why-are-s3-and-google-storage-bucket-names-a-global-namespace

1. The 17 Ways to Run Containers on AWS
    - https://www.lastweekinaws.com/blog/the-17-ways-to-run-containers-on-aws/

1. How to work with windows EC2?
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html

1. EC2 Instance Types
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html

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

1. http to https redirection in ELB?
    - https://aws.amazon.com/about-aws/whats-new/2018/07/elastic-load-balancing-announces-support-for-redirects-and-fixed-responses-for-application-load-balancer/

1. Specific use cases for Private ELB?
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-internal-load-balancers.html

1. AutoScaling using Custom Metrics
    - https://medium.com/qbits/autoscaling-using-custom-metrics-5f977903bc45
    - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html

1. Where do we specify the termination policy?
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html

1. Resource Groups
    - https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html

1. VPC Resize
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-resize

1. What is the least CIDR that we can use in AWS VPC?
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#VPC_Sizing

1. Mounting EFS by IP address
    - https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-ip-addr.html

1. EC2 accidental termination
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination

1. Does ELB works as forward or reverse proxy? Mainly used for load balancing, but can also be used for reverse proxy.
    - https://smartproxy.com/blog/the-difference-between-a-reverse-proxy-and-a-forward-proxy
    - https://www.sumologic.com/blog/aws-elb-vs-nginx-load-balancer/
    - https://www.trianz.com/insights/reverse-proxying-requests-with-aws-elb-edge
    - https://www.nginx.com/resources/glossary/reverse-proxy-vs-load-balancer/

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

1. Limits of the ELB
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html

1. AWS CLI V1 vs V2
    - https://www.youtube.com/watch?v=U5y7JI_mHk8

1. How many versions can store in S3?
    - https://docs.amazonaws.cn/en_us/AmazonS3/latest/dev/list-obj-version-enabled-bucket.html

1. Getting started with storage gateway
    - https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStarted.html

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

1. Cloud Patterns
    - https://docs.microsoft.com/en-us/azure/architecture/patterns/

1. How can I utilize user data to automatically execute a script with every restart of my Amazon EC2 instance?
    - https://aws.amazon.com/premiumsupport/knowledge-center/execute-user-data-ec2/

1. S3 Demo around Tagging
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-configuration-examples.html#lifecycle-config-ex1

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

1. Info on how to create a HA RDS
    - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
    - https://aws.amazon.com/blogs/database/amazon-rds-under-the-hood-multi-az/
    - https://www.youtube.com/watch?v=uiiS1h4PSI8

1. What is Cloud Native?
    - https://www.redhat.com/en/topics/cloud-native-apps

    >Cloud-native applications are a collection of small, independent, and loosely coupled services. They are designed to deliver well recognized business value, like the ability to rapidly incorporate user feedback for continuous improvement. In short, cloud-native app development is a way to speed up how you build new applications, optimize existing ones, and connect them all together. Its goal is to deliver apps users want at the pace a business needs.

1. Replacing Auto Scaling instances based on an instance refresh
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html

1. How can I automate Amazon EBS snapshot management using Amazon Data Lifecycle Manager?
    - https://aws.amazon.com/premiumsupport/knowledge-center/ebs-snapshot-data-lifecycle-manager/

1. Difference between LogGroup and LogStream in CloudWatch Logs
    - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html

1. Lambda functions as targets for Application ELB
    - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html

1. Attaching a volume to multiple instances with Amazon EBS Multi-Attach
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html

1. How do I set up weighted target groups for my Application Load Balancer?
    - https://aws.amazon.com/premiumsupport/knowledge-center/elb-make-weighted-target-groups-for-alb/

1. Connecting to Linux and Windows EC2 instances from Mac
    - https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac (for Windows EC2 instances)
    - https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/step-2-connect-to-instance.html (For Linux EC2 instances)

1. Hibernate EC2 instances
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html

# TODO

1. Categorize the questions based on services. Makes it easy to find the appropriate question.

2. May be use tags for categorizing the FAQ.

3. Delete the duplicates (use shell commands)