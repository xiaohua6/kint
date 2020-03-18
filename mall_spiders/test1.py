import pickle

from pymongo import MongoClient
import redis


def mongo_to_redis():


    redis_=redis.StrictRedis(db=0)
    mongo_=MongoClient()
    collect=mongo_['jd']['category']

    c=collect.find()
    for res in c:
        res=pickle.dumps(res)
        redis_.lpush('satrturljd',res)

    # res=redis_.rpop('satrturljd')
    length=redis_.llen('satrturljd')
    # res=pickle.loads(res)
    print(length)
    # mongo_.close()
    # print(res)
if __name__ == '__main__':
    mongo_to_redis()
