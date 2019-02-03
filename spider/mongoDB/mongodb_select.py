import pymongo
from bson.objectid import  ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['test']
collection = db['students']

result = collection.find_one({'name': 'James'})
print(type(result))
print(result)

result = collection.find_one({'_id':ObjectId('5bf0cc212694531aa49aaf13')})
print(result)

results = collection.find({})
print(results)
for result in results:
    print(result)

# 多条记录
results = collection.find({'age': 22})
print(results)
for result in results:
    print(result)

# 比较符号
results = collection.find({'age': {'$gt': 20}})
print(results)
for result in results:
    print(result)

print('======正则匹配======')
# 正则匹配
results = collection.find({'name': {'$regex': 'y.*'}})
print(results)
for result in results:
    print(result)

#计数
print('======计数======')
count = collection.count_documents({'age':{'$gt': 22}})
print(count)

#排序
print('======排序======')
results = collection.find().sort('age', pymongo.ASCENDING)
print([(result['name'], result['age']) for result in results])

#偏移
print('======偏移======')
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])
