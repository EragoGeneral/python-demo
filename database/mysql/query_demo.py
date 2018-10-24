import pymysql

conn = pymysql.connect('192.168.72.1', 'root', 'root', 'testdb')
cursor = conn.cursor()
cursor.execute('select * from userinfo where age >= %s and age <= %s', [25, 35])
print(cursor.rowcount)
data = cursor.fetchall()
print(data)
cursor.close()
conn.close()

