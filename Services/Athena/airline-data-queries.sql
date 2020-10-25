/*
Create a table in Athena ontime and map to the data in S3
Make sure to change the location of the S3 data
*/

create external table ontime (
  Year INT,
  Month INT,
  DayofMonth INT,
  DayOfWeek INT,
  DepTime  INT,
  CRSDepTime INT,
  ArrTime INT,
  CRSArrTime INT,
  UniqueCarrier STRING,
  FlightNum INT,
  TailNum STRING,
  ActualElapsedTime INT,
  CRSElapsedTime INT,
  AirTime INT,
  ArrDelay INT,
  DepDelay INT,
  Origin STRING,
  Dest STRING,
  Distance INT,
  TaxiIn INT,
  TaxiOut INT,
  Cancelled INT,
  CancellationCode STRING,
  Diverted STRING,
  CarrierDelay INT,
  WeatherDelay INT,
  NASDelay INT,
  SecurityDelay INT,
  LateAircraftDelay INT
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION 's3://airline-dataset-praveen/input/';

/*
Count the number of delayed flights for each of the origin on the CSV data
Note down the execution time and amount of data scanned
*/

select Origin, count(*) from ontime where DepTime > CRSDepTime group by Origin;

/*
Convert the CSV data to the Parqet data with the Snappy compression
Make sure to change the location of the S3 data
*/

CREATE TABLE ontime_parquet_snappy
    WITH (
          format = 'PARQUET',
          parquet_compression = 'SNAPPY',
          external_location = 's3://airline-dataset-praveen/athena-export-to-parquet'
    ) AS SELECT * FROM ontime;

/*
Count the number of delayed flights for each of the origin on the Parqet data with the Snappy compression
Note down the execution time and amount of data scanned
*/

select Origin, count(*) from ontime_parquet_snappy where DepTime > CRSDepTime group by Origin;