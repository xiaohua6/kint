from pymongo import MongoClient
client=MongoClient()
collection=client['python5']['stu']


print(collection.find_one({"name":"周瑜"}))

collection.delete_many({"name":"黄忠"})

c=collection.find()
for ret in c:
    print(ret)
