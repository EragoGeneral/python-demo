import pymysql

db = pymysql.connect(host='192.168.20.1', port=3306, user='root', password='root', db='spiders')
cursor = db.cursor()

sql = 'select * from students where age >= 20'

try:
    cursor.execute(sql)
    print('Count: ', cursor.rowcount)
    one = cursor.fetchone()
    print('One: ', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')


try:
    cursor.execute(sql)
    print('Count: ', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row: ', row)
        row = cursor.fetchone()
except:
    print('Error')

db.close()


