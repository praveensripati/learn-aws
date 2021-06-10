# Elastic File System

What is a EFS mount target?

https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-conceptual

A mount target provides an IP address for an NFSv4 endpoint at which you can mount an Amazon EFS file system. You mount your file system using its Domain Name Service (DNS) name, which resolves to the IP address of the EFS mount target in the same Availability Zone as your EC2 instance. You can create one mount target in each Availability Zone in an AWS Region. If there are multiple subnets in an Availability Zone in your VPC, you create a mount target in one of the subnets. Then all EC2 instances in that Availability Zone share that mount target.

1. Create two EC2 instances (Ubuntu/t2.micro) with AllowSSH (inbound/SSH/22) Security Group.

1. Create EFS Volume with the mount target in the AZ as the EC2 instances and AllowEFS (inbound/NFS) as the Security Group.

1. Execute the below commands to mount the EFS on both the EC2 instances.

    >sudo su\
    >apt-get update\
    >apt-get install nfs-common -y

    >mkdir ~/efs-mount-point

    >#Make sure to replace the IP with the IP address of the mount target from the same AZ where the EC2 has been created.\
    >mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport **172.31.31.82**:/   ~/efs-mount-point

    > cd ~/efs-mount-point

1. Create a file on the first EC2 and access the same from the second EC2 using the below commands.

    >echo "Welcome to AWS" > somefile.txt\
    >cat somefile.txt

1. If the above works then we know that both the EC2 are using a common File System.

# Further Reading

1. Mount the Amazon EFS File System on the EC2 Instance and Test
    - https://docs.aws.amazon.com/efs/latest/ug/wt1-test.html