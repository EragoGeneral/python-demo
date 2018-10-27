import pymysql

#  pip install pymysql

conn = pymysql.connect('192.168.72.1', 'root', 'root', 'testdb')
cursor = conn.cursor()
cursor.execute('insert into userinfo(name, age) values(%s, %s)', ['Antony', 24])
print(cursor.rowcount)
conn.commit()

cursor.close()
conn.close()