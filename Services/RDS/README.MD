# Relational Database Service

## Steps for creating an RDS Instance (MySQL) and connecting to it.

1. Create a Security Group with port 3306 inbound allowed.

1. Create RDS instance.
	- From the RDS Management Console Go to Dashboard and click on `Create Database`.
	- Select MySQL and click Next.
	- Select Dev/Test - MySQL.
	- Select the instance class as `db.t2.micro`.
    - Select the Security Group created earlier.
	- Specify the DB instance identifier as mydbinstance, username and password. Click on next. Don't forget them.
    - Disable the storage AutoScaling.
    - Change the database visibility to Public.
	- Disable the backups.
	- Click on Create database. It will take around 5min to create the database.

1. Download SQL client to connect to RDS. And install it.
https://www.heidisql.com/

1. In the HeidiSQL Client.
    - Enter the endpoint got from RDS Management Console.
    - Enter the user name/password
    - Click on open to connect to RDS in Cloud.

1. Select the myrecipiesdb on left pane. Go to the Query Tab and run the below queries.
    ```
    CREATE TABLE recipies (
    recipe_id INT NOT NULL,
    recipe_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (recipe_id),
    UNIQUE (recipe_name)
    );

    INSERT INTO recipies
    (recipe_id, recipe_name)
    VALUES
        (1,"Tacos"),
        (2,"Tomato Soup"),
        (3,"Grilled Cheese");

    select * from recipies;
    ```
5. Delete the RDS Database.
	- Unselect "Create final snapshot?"
    - Select "I acknowledge"

# Further Reading

1. Another way to connect using the IAM credentials. How do I allow users to connect to an Amazon RDS MySQL DB instance using their IAM credentials?
    - https://aws.amazon.com/premiumsupport/knowledge-center/users-connect-rds-iam/

# TODO