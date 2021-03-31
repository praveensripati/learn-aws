AutoScaling is all about adding and removing the AWS resources automatically based on on a certain conditions using the average CPU usage, network usage or some application level metrics like the number of users logged into the application or number of transactions in the application.

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
