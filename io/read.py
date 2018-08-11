#! /usr/bin/env  python3
# -*- coding:utf-8  -*-

with open('G:/mine/study/workspace/python/demo/file/1.txt', 'r', encoding='utf-8', errors='ignore') as file:
  for line in file.readlines():
      print(line.strip())

f = open('G:/mine/study/workspace/python/demo/file/礼盒口红4.jpg', 'rb')
# print(f.read())  显示二进制字符串
f.close()

    