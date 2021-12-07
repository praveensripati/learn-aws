# Overall Steps

1. Push the images to the ECR.

1. Create an IAM Role for ECR Tasks with AWSAppMeshEnvoyAccess Policy.

1. Create ECS Cluster, TaskDef and Services with discovery.
    - Enable Service Discovery (person.com namespace)

1. Create all the App Mesh components using CFN.

1. Include AppMesh integration in the Taskdef.

1. Update the ECS Services with the new Taskdef.

# REST URL

http://3.82.221.49:9000/person/all
http://3.82.221.49:9000/person/get/1

# NodeJS REST Server

nodejs-rest-server
nodejs-rest-server-service.person.com

cd code/nodejs-rest-server
docker build . -t nodejs-rest-server
aws ecr create-repository --repository-name nodejs-rest-server --region us-east-1
docker run -dit --name nodejs-rest-server -p 9000:80 nodejs-rest-server

# NodeJS REST Server (V2)

nodejs-rest-server-v2
nodejs-rest-server-v2-service.person.com

cd code/nodejs-rest-server-v2
docker build . -t nodejs-rest-server-v2
aws ecr create-repository --repository-name nodejs-rest-server-v2 --region us-east-1
docker run -dit --name nodejs-rest-server-v2 -p 9000:80 nodejs-rest-server-v2

# NodeJS REST Client

nodejs-rest-client
nodejs-rest-client-service.person.com

cd code/nodejs-rest-client
docker build . -t nodejs-rest-client
aws ecr create-repository --repository-name nodejs-rest-client --region us-east-1
docker run -dit --name nodejs-rest-client -p 8080:80 nodejs-rest-client

# Command to increase/decrease the number of tasks in a service

aws ecs update-service --cluster mycluster --service nodejs-rest-server-service --desired-count 1
aws ecs update-service --cluster mycluster --service nodejs-rest-server-v2-service --desired-count 1
aws ecs update-service --cluster mycluster --service nodejs-rest-client-service --desired-count 1

aws ecs update-service --cluster mycluster --service nodejs-rest-server-service --desired-count 0
aws ecs update-service --cluster mycluster --service nodejs-rest-server-v2-service --desired-count 0
aws ecs update-service --cluster mycluster --service nodejs-rest-client-service --desired-count 0

