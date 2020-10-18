import redis
import mysql.connector
import sys

redis_url = 'myrediscluster.hwzwnc.0001.use1.cache.amazonaws.com'

host = 'database-1.cmeeo0ikklen.us-east-1.rds.amazonaws.com'
user = 'praveen'
password = 'praveen123'
database = 'customer_db'

r = redis.StrictRedis(host=redis_url, port=6379,
                      charset="utf-8", decode_responses=True)

if r.get(sys.argv[1]) is None:

    print("The TUPLE is not there in ElastiCache")

    # Connect to the RDS MySQL Instance
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, database=database)
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT * FROM customers where name = \"" + sys.argv[1] + "\"")
    myresult = mycursor.fetchone()

    if myresult is not None:
        print("Got from the Database, so writing TUPLE to ElastiCache")
        r.set(myresult[0], myresult[1])
    else:
        print("Not there in the Database")

else:
    print("The TUPLE is there in ElastiCache")
