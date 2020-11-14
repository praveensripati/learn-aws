# Elastic File System

1. Create two EC2 instances (Ubuntu/t2.micro) with AllowSSH (inbound/SSH/22) and AllowNFS (inbound/NFS) Security Groups.

1. Create EFS Volume with the mount target in the AZ as the EC2 instances and AllowEFS as the Security Group.

1. Execute the below commands to mount the EFS on both the EC2 instances.

    >sudo su\
    >apt-get update\
    >apt-get install nfs-common -y

    >mkdir ~/efs-mount-point

    >#Make sure to replace the IP with the IP address of the mount target\
    >mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport **172.31.31.82**:/   ~/efs-mount-point

    > cd ~/efs-mount-point

1. Create a file on the first EC2 and access the same from the second EC2 using the below commands.

    >echo "Welcome to AWS" > somefile.txt
    >cat somefile.txt

1. If the above works then we know that both the EC2 are using a common File System.

# Further Reading

1. Mount the Amazon EFS File System on the EC2 Instance and Test
    - https://docs.aws.amazon.com/efs/latest/ug/wt1-test.html