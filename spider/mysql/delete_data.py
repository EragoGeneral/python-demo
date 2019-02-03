import pymysql

db = pymysql.connect(host='192.168.20.1', port=3306, user='root', password='root', db='spiders')
cursor = db.cursor()

table = 'students'
condition = ' age > 28'

sql = 'delete from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()