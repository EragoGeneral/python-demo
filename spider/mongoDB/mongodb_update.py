import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['test']
collection = db['students']

condition = {'_id': ObjectId('5bf0cc202694531aa49aaf12')}
student = collection.find_one(condition)
student['name'] = 'Kevin'
student['age'] = 25
student['id'] = '20170104'
result = collection.update_one(condition, {'$set': student})
print(result.raw_result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gte': 20}}
result = collection.update_many(condition, {'$inc': {'age': 2}})
print(result)
print(result.matched_count, result.modified_count)

condition = {'_id': ObjectId('5bf0cc68269453106c92d05b'), 'name': 'Paul'}
result = collection.update_one(condition, {'$set': {'name': 'Paul', 'age': 29, 'id': '20170101'}})
print(result.modified_count, result.matched_count)





