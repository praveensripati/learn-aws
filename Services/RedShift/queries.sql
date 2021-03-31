/*
Create the users table
*/

create table users(
	userid integer not null distkey sortkey,
	username char(8),
	firstname varchar(30),
	lastname varchar(30),
	city varchar(30),
	state char(2),
	email varchar(100),
	phone char(14),
	likesports boolean,
	liketheatre boolean,
	likeconcerts boolean,
	likejazz boolean,
	likeclassical boolean,
	likeopera boolean,
	likerock boolean,
	likevegas boolean,
	likebroadway boolean,
	likemusicals boolean);

/*
Load the data in the users table
Make sure to replace the iam_role ARN
*/

copy users
from 's3://awssampledbuswest2/tickit/allusers_pipe.txt' 
iam_role 'arn:aws:iam::304000509264:role/Role4RS-S3RO' 
delimiter '|' region 'us-west-2';

/*
Run queries on users table
*/

select count(*) from users;