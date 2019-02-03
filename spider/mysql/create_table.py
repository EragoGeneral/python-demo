import pymysql

db = pymysql.connect(host='192.168.20.1', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
sql = 'create table if not exists students(id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))'
cursor.execute(sql)
db.close()