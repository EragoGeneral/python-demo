﻿# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('select * from user where id = ?', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor:
cursor.close()
# 关闭Connection:
conn.close()