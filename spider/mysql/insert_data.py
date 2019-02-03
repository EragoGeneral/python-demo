import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='192.168.20.1', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
sql = 'insert into students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()


db = pymysql.connect(host='192.168.20.1', port=3306, user='root', password='root', db='spiders')
cursor = db.cursor()

data = {
    'id': '20120004',
    'name': 'Nask',
    'age': 25
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'insert into {table}({keys})values({values})'.format(table=table, keys=keys, values=values)

try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
