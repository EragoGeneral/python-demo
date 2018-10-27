import pymysql

conn = pymysql.connect('192.168.72.1', 'root', 'root', 'testdb')
cursor = conn.cursor()

cursor.execute('update userinfo set name = %s where id = %s', ['Admin', 2])
print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()