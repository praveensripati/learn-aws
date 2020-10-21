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

1. Home Page
   - https://aws.amazon.com/elasticache/

1. Cache 101
   - https://cloudonaut.io/caching-on-aws-101/

1. Comparing Memcached and Redis
   - https://aws.amazon.com/elasticache/redis-vs-memcached/
   - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SelectEngine.html

1. UseCases
   - https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/elasticache-use-cases.html

1. Integrating Memcached with WordPress
   - https://aws.amazon.com/elasticache/memcached/wordpress-with-memcached/ 

1. Getting started with Memcached
   - https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/GettingStarted.html

1. Connecting to the node through Telnet
   - https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/nodes-connecting.html
   - https://www.tutorialspoint.com/memcached/memcached_add_data.htm

1. Interfacing with Memcached
   - https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/nodes-connecting.html
   - https://www.tutorialspoint.com/memcached/memcached_add_data.htm