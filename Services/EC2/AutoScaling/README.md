# Auto Scaling

AutoScaling is all about adding and removing the AWS resources automatically based on on a certain conditions using the average CPU usage, network usage or some application level metrics like the number of users logged into the application or number of transactions in the application.

# Practice

1. In the EC2 Management Console navigate to and create a Launch Template. Make sure to enable the detailed monitoring.
![](images/2021-04-21-13-00-22.png)
![](images/2021-04-21-13-04-17.png)
![](images/2021-04-21-13-05-32.png)

1. From the same EC2 Management Console, create an Auto Scaling Group.
![](images/2021-04-21-13-07-11.png)
![](images/2021-04-21-13-08-28.png)
![](images/2021-04-21-13-09-21.png)
![](images/2021-04-21-13-09-50.png)
![](images/2021-04-21-13-10-21.png)
![](images/2021-04-21-13-11-02.png)

1. The Auto Scaling Group and an EC2 instance would also be created as shown below. Name the EC2 instance as `1`.
![](images/2021-04-21-13-12-38.png)
![](images/2021-04-21-13-23-34.png)

1. Create ScaleUp Policy for the Auto Scaling Group by clicking on `Add policy`.
![](images/2021-04-21-13-24-52.png)

1. Click on `Create a CloudWatch alarm` to open a new tab.
![](images/2021-04-21-13-26-24.png)
![](images/2021-04-21-13-27-31.png)

1. Select EC2 -> By Auto Scaling Group. Filter by the Auto Scaling Group name and select `CPUUtilization`. Click on `Select metric`.
![](images/2021-04-21-13-29-36.png)

1. Specify the metrics condition as shown below.
![](images/2021-04-21-13-31-03.png)
![](images/2021-04-21-13-31-26.png)

1. Under `Configure actions` remove the actions. We will add it later.
![](images/2021-04-21-13-32-35.png)

1. Give some name to the Alarm. Preview and create the Alarm.
![](images/2021-04-21-13-33-26.png)
![](images/2021-04-21-13-34-51.png)

1. Go back to the `Create scaling policy` and select the alarm and the action as shown below and create the scaling policy.
![](images/2021-04-21-13-36-34.png)
![](images/2021-04-21-13-37-30.png)

1. Connect to the first EC2 instance and increase the CPU using the below `dd ....` command. Notice the increase in the CPU from the output of the `top` command.
![](images/2021-04-21-13-40-55.png)

1. Notice the change in the status of the CloudWatch Alarm. Initially it would be in the `OK` state, but as the EC2 instance CPU increases it changes to `ALARM` state. 
![](images/2021-04-21-13-44-00.png)

1. Notice the increase in the number of EC2 instances in a few minutes.
![](images/2021-04-21-13-45-35.png)
![](images/2021-04-21-14-09-30.png)
![](images/2021-04-21-14-10-10.png)

1. Killing the dd command (Ctrl+C) will drop the CPU, but won't decrease the EC2 instance as the scale down policy has not been set.

1. Delete the Auto Scaling Group. This will automatically delete the EC2 instances.

# Further Reading

1. To increase the CPU on a Linux EC2 instance. The same can be checked using the top command.
   >dd if=/dev/urandom | bzip2 -9 >> /dev/null

    A few other ways are mentioned in the below StackOverflow post.\
    http://stackoverflow.com/questions/2925606/how-to-create-a-cpu-spike-with-a-bash-command

1. How the instances are terminated.
    - http://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-termination.html

1. Lifecycle Hooks.
    - http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html

1. Auto Scaling Cooldowns.
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html

1. Different AutoScaling Types.
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html#as-scaling-types

1. AutoScaling using Launch Templates.
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchTemplates.html
     -https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html

1. AutoScaling with LaunchConfigurations.
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-register-lbs-with-asg.html#as-register-lbs-console
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#policy_creating

1. Controlling Which Auto Scaling Instances Terminate During Scale In.
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#custom-termination-policy

1. AutoScaling based on the SQS Queue depth.
    - https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/
    - https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html

1. Scaling your applications faster with EC2 Auto Scaling Warm Pools
    - https://aws.amazon.com/blogs/compute/scaling-your-applications-faster-with-ec2-auto-scaling-warm-pools/
