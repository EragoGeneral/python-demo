import pymysql

db = pymysql.connect('192.168.20.1', user='root', password='root', port = 3306)
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchall()
print('Database version: ', data)
cursor.execute('create database spiders default character set utf8')
db.close()
