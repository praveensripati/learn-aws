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