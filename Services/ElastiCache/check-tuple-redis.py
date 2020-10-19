import redis
import sys

redis_url = 'myrediscluster.hwzwnc.0001.use1.cache.amazonaws.com'

r = redis.StrictRedis(host=redis_url, port=6379,
                      charset="utf-8", decode_responses=True)

if r.get(sys.argv[1]) is None:
    print("The TUPLE is not there in ElastiCache")
else:
    print("The TUPLE is there in ElastiCache")
