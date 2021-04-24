# Installing Docker On Ubuntu and creating an image

1. Create an Ubuntu EC2 and connect to it.

1. Make sure that Docker and related softwares are not installed on the Ubuntu EC2.
    >sudo apt-get remove docker docker-engine docker.io containerd runc

1. Install the prerequisites for Docker.
    >sudo apt-get update\
    >sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y

1. Add the Docker repository.
    >curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -\
    >sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

1. Install Docker on Ubuntu EC2.
    >sudo apt-get update\
    >sudo apt-get install docker-ce docker-ce-cli containerd.io -y

1. Give permissions for the non-root `ubuntu` user to interact with Docker.
    >sudo usermod -a -G docker ubuntu\
    >newgrp docker

1. Copy the `Dockerfile` to the EC2 instance. This files takes the base Ubuntu image and installs apache2 and create a simple webpage.

1. Build the Docker image.
    >docker build -t hello-world .\
    >docker images --filter reference=hello-world

1. Execute the Docker image. Ignore the error message around FQDN while executing.
    >docker run -t -i -p 80:80 hello-world

1. Access the webpage from the browser. Use the EC2 Public IP address along with th port number.

1. Stop the container using `Ctrl+C`.

# Further Reading

1. Docker basics around AWS
    - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html