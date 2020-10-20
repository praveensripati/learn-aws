create table ontime (
  Year integer,
  Month integer,
  DayofMonth integer,
  DepTime  integer,
  CRSDepTime integer,
  Origin varchar(120),
  Dest varchar(120)
);

copy ontime
from 's3://praveen-airline/data.txt' 
iam_role 'arn:aws:iam::304000509264:role/Role4RedShift-S3RO' 
delimiter ',' region 'us-east-1';

select Origin, count(*) as Count from ontime where DepTime > CRSDepTime group by Origin order by Count desc;