import pymysql

sql = 'update students set age = %s where name = %s'
db = pymysql.connect(host='192.168.20.1', port=3306, user='root', password='root', db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql, (20, 'Bob'))
    db.commit()
except:
    db.rollback()
db.close()


data = {
    'id': '20120003',
    'name': 'Jordan',
    'age': 29
}


db = pymysql.connect(host='192.168.20.1', port=3306, user='root', password='root', db='spiders')
cursor = db.cursor()
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))

sql = 'insert into {table}({keys}) values({values}) on duplicate key update '.format(table=table, keys=keys,values=values)
update = ','.join([" {key}=%s".format(key=key) for key in data])
sql += update
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()