import json

d = dict(name='Bob', age=20, score=88)

obj = json.dumps(d)

print(obj)

json_str = '{ "age":20, "score":88, "name":"Bob"}'
obj1 = json.loads(json_str)
print(obj1)