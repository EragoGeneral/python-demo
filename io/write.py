#! /usr/bin/env  python3
# -*- coding:utf-8  -*-

f = open('G:/mine/study/workspace/python/demo/file/2.txt', 'w', encoding='utf-8')
f.write('你好 world!')
f.close()


with open('G:/mine/study/workspace/python/demo/file/2.txt', 'a', encoding='utf-8') as file:
    file.write('\n学习 python!')
	
	