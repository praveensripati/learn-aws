# AWS App Mesh

 `Service Mesh` is a new software layer that handles all of the communications between services. It provides new features to connect and manage connections between services and is independent of each service’s code, allowing it to work across network boundaries and with multiple service management systems. AWS App Mesh is a managed serviced provided by AWS around Service Mesh.

`AWS App Mesh` is a new technology that makes it easy to monitor, control, and debug the communications between services. App Mesh separates the logic needed for monitoring and controlling communications into a proxy that runs next to every service. This removes the need to coordinate across teams or update application code to change how monitoring data is collected or traffic is routed. This allows you to quickly pinpoint the exact location of errors and automatically reroute network traffic when there are failures or when code changes need to be deployed.

Envoy proxy has to be added to the Amazon ECS task, Kubernetes pod, or Amazon EC2 instance represented by your App Mesh endpoint, such as a virtual node or virtual gateway. 

![](images/envoy-proxy.png)

Consider the following simple example application, that doesn’t use App Mesh. The two services can be running on AWS Fargate, Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), Kubernetes on Amazon Elastic Compute Cloud (Amazon EC2) instances, or on Amazon EC2 instances with Docker.

![](images/normal-application.png)

In this illustration, both serviceA and serviceB are discoverable through the apps.local namespace. Let's say, for example, you decide to deploy a new version of serviceb.apps.local named servicebv2.apps.local. Next, you want to direct a percentage of the traffic from servicea.apps.local to serviceb.apps.local and a percentage to servicebv2.apps.local. When you're sure that servicebv2 is performing well, you want to send 100 percent of the traffic to it.

App Mesh can help you do this without changing any application code or registered service names. If you use App Mesh with this example application, then your mesh might look like the following illustration.

![](images/appmesh-application.png)
![](images/appmesh-components.png)

App Mesh benefits (https://www.appmeshworkshop.com/introduction/appmesh_benefits/)\
    - End-to-end visibility\
    - Ensure high availability\
    - Streamline operations\
    - Enhance any application\
    - End-to-end Encryption

# Further Reading

1. What Is AWS App Mesh?
    - https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html

1. App Mesh best practices
    - https://docs.aws.amazon.com/app-mesh/latest/userguide/best-practices.html

1. Getting started with App Mesh
    - https://docs.aws.amazon.com/app-mesh/latest/userguide/getting-started.html

# App Mesh in Practice

1. AWS App Mesh Examples
    - https://github.com/aws/aws-app-mesh-examples

1. Getting started with AWS App Mesh and Amazon EKS (uses the above git code)
    - https://aws.amazon.com/blogs/containers/getting-started-with-app-mesh-and-eks/

1. App Mesh Workshop
    - https://www.appmeshworkshop.com/

1. AWS App Mesh VS. Istio
    - https://vedcraft.com/architecture/aws-appmesh-vs-istio-comparison-of-service-mesh/

1. Microservices with AWS ECS (Includes Fargate/AppMesh/XRay) (is a bit patchy, but has the console screens)
    - https://medium.com/swlh/microservices-with-aws-ecs-58dd5006ab2e
    - https://medium.com/swlh/microservices-and-aws-app-mesh-f4c7cab9ddca
    - https://medium.com/swlh/monitor-microservices-using-aws-x-ray-c472916ac0bd

1. Create a pipeline with canary deployments for Amazon ECS using AWS App Mesh
    - https://aws.amazon.com/blogs/containers/create-a-pipeline-with-canary-deployments-for-amazon-ecs-using-aws-app-mesh/