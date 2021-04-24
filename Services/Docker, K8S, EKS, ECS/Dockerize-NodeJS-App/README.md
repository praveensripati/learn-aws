# Dockerizing a NodeJS Application

1. Copy the `Dockerize-NodeJS-App` folder and its contents to Ubuntu EC2.

1. On the EC2 instance `cd` to that folder and build the docker image.
    >docker build -t praveen/node-web-app .

1. The image would be created in a few minutes, check if the image has been created or not.
    >docker images

1. Run the Docker image and expose the port 8080 of the container on port 49160 on the EC2 instance.
    >docker run -p 49160:8080 -d praveen/node-web-app

1. Check the status of the container.
    >docker ps

1. Access the webpage from the Docker image.
    >curl -i localhost:49160
![](images/dockerize-nodejs-web-app-command.png)

1. Grab the Public IP address of the EC2 instance and access the web page via the browser. Make sure to use the port 49160 and the same is allowed in the Security Group attached to the EC2.\
![](images/dockerize-nodejs-web-app-browser.png)