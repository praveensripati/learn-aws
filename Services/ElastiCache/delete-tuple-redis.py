import redis
import sys

redis_url = 'my-demo-redis.jmgrvh.ng.0001.use1.cache.amazonaws.com'

r = redis.StrictRedis(host=redis_url, port=6379,
                      charset="utf-8", decode_responses=True)
r.delete(sys.argv[1])

print("Deleted a TUPLE to Redis")
