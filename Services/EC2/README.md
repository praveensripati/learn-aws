# Python program to interact with Redis

1. Create an Ubuntu EC2 instance (t2.micro) and connect to to it.

1. Execute the below commands on the EC2 instance.

    1. Become root
       >sudo su

    1. Get the list of softwares
       >apt-get update

    1. Install python and pip\
       >apt-get install python2.7 python-pip -y

    1. Install the redis connector for python\
       >pip install redis

1. Create an ElastiCache Cluster (cache.t2.micro) and get the endpoint once the cluster has been created. Make sure to attach the appropriate Security Group to the ElastiCache Cluster. 

1. In the below python file change the redis_url with the above endpoint. Copy the python code to the EC2 with the same filename.

    1. check-tuple.py
    1. delete-tuple.py
    1. insert-tuple.py

1. Execute the below command to insert a tuple in the ElastiCache Redis Cluster.
    >python insert-tuple-redis.py age 25

1. Get the tuple back from the ElastiCache Redis Cluster. It should return 25.
   >python check-tuple-redis.py age

1. Delete the tuple from the ElastiCache Redis Cluster.
   >python delete-tuple-redis.py age

1. Try to delete the tuple "age" and it shouldn't return anything.

1. Make sure to terminate the EC2 and the ElastiCache Cluster.

# Further Reading

https://aws.amazon.com/elasticache/

