# Creating a website on Linux EC2

1. Create a Security Group (Add inbound rule, open port 22 and 80 for anywhere)

1. Create a KeyPair and download the .ppk file.

1. Launch an EC2 with the below options. Rest of the options can be left default.
	- Search for "Ubuntu Server 18.04 LTS" and select the first AMI
	- t2.micro (free tier)
	- Use the above created SecurityGroup and the KeyPair

1. Get the Public IP from the Web Console for the EC2.

1. Use Putty to login. In the putty provide
	- username and IP (ubuntu@1.2.3.4)
	- .ppk file location (Connection -> SSH -> Auth)

1. Create a small website using the below commands

    >#become a root\
    >sudo su

    >#get the list of softwares\
    >apt-get update

    >#install the apache2 webserver\
    >apt-get install apache2 -y

    >#start apache2\
    >service apache2 start

    >#move to the default html folder\
    >cd /var/www/html

    >#delete the existing index.html\
    >rm index.html

    >#create a new index.html\
    >echo "Hello, world!" > index.html

1. Access the webpage using the IP address of EC2 in the browser.

1. Modify the Security Group to remove port 80 and the webpage should not be accessible. 