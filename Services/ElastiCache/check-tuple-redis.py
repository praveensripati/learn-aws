import redis
import sys

redis_url = 'my-demo-redis.jmgrvh.ng.0001.use1.cache.amazonaws.com'

r = redis.StrictRedis(host=redis_url, port=6379,
                      charset="utf-8", decode_responses=True)

if r.get(sys.argv[1]) is None:
    print("The TUPLE is not there in Redis")
else:
    print("The TUPLE is there in Redis")
