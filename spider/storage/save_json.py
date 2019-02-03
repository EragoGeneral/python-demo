import json

str = '''
[{
"name":"Bob",
"gender":"male",
"birthday":"1992-10-18"
},{
"name":"Selina",
"gender":"female",
"birthday":"1995-10-18"
}]
'''

print(type(str))
data = json.loads(str)
print(data)
print(type(data))

print(data[0]['name'])
print(data[0].get('name'))

print(data[0].get('age'))
print(data[0].get('age', 25))

print('Load json file======')
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)


print('save json file======')
data = [{
"name":"Bob",
"gender":"male",
"birthday":"1992-10-18"
},{
"name":"Selina",
"gender":"female",
"birthday":"1995-10-18"
}]
with open('data1.json', 'w') as file:
    # 代表缩进字符个数， 格式化 json
    file.write(json.dumps(data, indent=2))

print('写入中文字符======')
data = [{
    "name": "王伟",
    "gender": "男",
    "birthday": "1992-10-18"
}]

with open('data2.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))