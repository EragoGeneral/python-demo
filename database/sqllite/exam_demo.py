# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

'''
def format_name(s):
    s1=s[0:1].upper()+s[1:].lower();
    return s1;
 
print(list(map(format_name, ['adam', 'LISA', 'barT'])))
'''

def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select name from user where score >= ? and score <= ? order by score', (low, high))    
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()
    
    return  list(map(lambda x:x[0], values))

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')

