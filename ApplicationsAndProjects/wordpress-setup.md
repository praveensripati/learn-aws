# WordPress Setup on AWS

[WordPress](https://wordpress.org/) is a very popular CMS (Content Management System) and is widely used to build blogs, sites etc. This page is about setting up WordPress on AWS.

**Option 1** : Install it using AWS Elastic BeanStalk as mentioned below. Note that this option is a bit costly than the other.

	>https://aws.amazon.com/getting-started/projects/build-wordpress-website/
	
**Option 2** : Install the different components manually.

1. Create EC2 (Ubuntu Server 18.04 LTS (HVM), SSD Volume Type) of type t2.micro
	
1.  Create a public RDS instance of db.t2.micro type using MySQL database. Note down the username, password, database and the RDS endpoint.
	
1. Note that all the commands have to be run as root. So execute the below command.
   >sudo su 

1. Putty into the EC2 instance and execute the below commands to install the prerequisies for WordPress.
   >apt-get update
   >apt-get install apache2 php php-mysql php-curl mysql-client libapache2-mod-php unzip -y

1. Again in Putty execute the below commands to download and extract the latest WordPress.
   >cd /var/www/
   >wget https://wordpress.org/latest.zip
   >unzip latest.zip

1. Make a copy of the wp-config-sample.php file as wp-config.php in Putty.
   >cd wordpress
   >cp wp-config-sample.php wp-config.php
		
1. Modify the wp-config.php to include the database details. The localhost should be replaced with the endpoint of the RDS database instance. Use the vi editor for the same.	
   >define('DB_NAME', 'database_name_here');
   >define('DB_USER', 'username_here');
   >define('DB_PASSWORD', 'password_here');
   >define('DB_HOST', 'localhost');
		
1. By default the webserver expects the web pages in the /var/www/html folder, but the WordPress has been installed in the /var/www/wordpress folder. Modify the 000-default.conf file in the /etc/apache2/sites-enabled folder to change the DocumentRoot to /var/www/wordpress.
		
1. For the changes to take effect the apache web server has to be restarted. Execute the below command.
	>service apache2 restart
		
1. (Optional) All the wordpress files belong to the root user and group. Change the permissions using the chown command.
	>chown -R www-data:www-data /var/www/wordpress
		
1. Access the WordPress using the below URL in a browser. Note to replace the ip address in the URL with public ip address of the EC2.
	>http://52.90.49.139/wp-admin/install.php
		
1. Complete the WordPress installation by following the instructions in the browser.

1. Once the installation is complete, log in to the WordPress and publish a new post.

## Additional tasks 

1. Create an ANAME record for the EC2 public ip address in the Route53 service. Now the WordPress blog can be accessed by using a user friendly URL. For this a domain needs to be registered.

1. Change the DB to multi AZ HA mode.

1. Create an EFS and attach it to Ubuntu instance (/var/www/wordpress/wp-content/uploads). Make sure all the WordPress media files go into the EBS folder.

1. Creating an AutoScaling WebSite along with ELB.

1. Create a highly available website by using ELB.
		
1. Use CloudFormation for automation.
