# Attaching new EBS to Linux EC2

1. Create an EC2 Linux instance

1. Create an EBS Drive of 1 GB and attach it to the above EC2 instance. EC2 and EBS should be in the same AZ.

1. Login to the EC2 instance and execute the below commands.

	- Become an administrator
      >sudo su
	
	- Determine where the 1 GB volume is (should be like /dev/xvdf).
      >fdisk -l
	
	- Format the disk with the file system.
      >mkfs /dev/xvdf
	
	- Create a directory
      >mkdir /mnt/disk100
	
	- Map or mount the disk to the folder.
      >mount /dev/xvdf /mnt/disk100
	
	- Create a file in the /mnt/disk100 folder.
      >echo "Welcome to AWS" > /mnt/disk100/file.txt
	
	- Check if the file has been created or not.
      >cat /mnt/disk100/file.txt

4. Terminate the EC2 instance. The 1GB Volume should be still there.

5. Create a new EC2 instance and attach the earlier created EBS volume. Run all the above commands except for the format.

6. Check if the file created earlier is present - "cat /mnt/disk100/file.txt"

7. Terminate the EC2 instance and delete the EBS volume.

# Further Reading

1. How many EBS can be attached to EC2?
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html

1. How to attach EBS to Windows EC2?
    - https://aws.amazon.com/premiumsupport/knowledge-center/attach-ebs-running-windows/

1. How many EC2's can be attached to a single EBS volume?
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html

1. How to extend a existing EBS for Windows and Linux?
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-modify-volume.html
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/recognize-expanded-volume-windows.html
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html

1. Using EBS Snapshot in some other regions
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html

1. Attach a root EBS Volume to a new EC2
    - https://www.youtube.com/watch?v=C6lSCAVggFE
    - https://stackoverflow.com/questions/6377669/can-i-change-the-root-ebs-device-of-my-amazon-ec2-instance

1. EBS Mirroring can be done using RAID
    - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/raid-config.html
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/raid-config.html

1. How can I automate Amazon EBS snapshot management using Amazon Data Lifecycle Manager?
    - https://aws.amazon.com/premiumsupport/knowledge-center/ebs-snapshot-data-lifecycle-manager/

1. Attaching a volume to multiple instances with Amazon EBS Multi-Attach
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html

1. Downloading and Exploring AWS EBS Snapshots
    - https://rhinosecuritylabs.com/aws/exploring-aws-ebs-snapshots/