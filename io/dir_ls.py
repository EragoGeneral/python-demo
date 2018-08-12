# -*-  coding:utf-8  -*-

import os

import datetime

for x in os.listdir('.'):
    flag, size = ('<DIR>', '')  if os.path.isdir(x) else ('', os.path.getsize(x))
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(x)).strftime('%Y-%m-%d %H:%M')
   # flag = '<DIR>' if os.path.isdir(x) else ''
    print('%10s\t%10s\t%10s\t%10s' % (mtime, flag, size, x))