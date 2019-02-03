import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['test']
collection = db['students']
result = collection.remove({'name': 'Jordan'})
print(result)

result = collection.delete_one({'name': 'Bryant', 'age': 31, '_id': ObjectId('5bf0cc68269453106c92d05c')})
print(result.deleted_count)

