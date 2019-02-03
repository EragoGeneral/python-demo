import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
# client1 = pymongo.MongoClient('mongodb://localhost:27017')

db = client.test
# db = client['test']

collection = db.students
# collection = db['students']

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_one(student)
print(result)
print(result.inserted_id)

student1 = {
    'id': '20170102',
    'name': 'James',
    'age': 22,
    'gender': 'male'
}
student2 = {
    'id': '20170103',
    'name': 'Bryant',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result.inserted_ids)



