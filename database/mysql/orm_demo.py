#!/usr/bin/python3
#coding:utf-8

#    pip install sqlalchemy   ;   pip install mysql-connector-python

from sqlalchemy import Column, String, Integer, Float, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象

class User(Base):
    # 表的名字
    __tablename__ = 'userinfo'
    # 表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    price = Column(Float)
    user_id = Column(Integer, ForeignKey('userinfo.id'))

# 初始化数据链接
engine = create_engine('mysql+mysqlconnector://root:root@192.168.72.1:3306/testdb')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

'''   新增用户
# 创建session对象
session = DBSession()
# 创建新 user 对象
new_user = User(name='Jenny', age=29)
# 添加到 session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()
'''


session = DBSession()
user = session.query(User).filter(User.id==1).one()
print('type', type(user))

print('name', user.name)
print('age', user.age)
print('book', list(map(lambda x:(x.id, x.name, x.price), user.books)))