import redis
import sys

redis_url = 'my-demo-redis.jmgrvh.ng.0001.use1.cache.amazonaws.com'

r = redis.StrictRedis(host=redis_url, port=6379,
                      charset="utf-8", decode_responses=True)
r.set(sys.argv[1], sys.argv[2])

print("Inserted a TUPLE to Redis")
