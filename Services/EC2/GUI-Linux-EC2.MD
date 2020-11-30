# Installing UI with Ubuntu EC2

1. Create an Ubuntu EC2 (18.04, for some reason 20.04 is not working)

1. Open RDP and SSH in inbound for the Security Group

1. Become root and install the required packages
    >sudo su\
    >apt-get update\
    >apt-get install -y xrdp xfce4 gedit -y\
    >service xrdp restart

1. Change the password for root or ubuntu
    >passwd ubuntu\
    >passwd root

1. Use RDP to connect as Ubuntu