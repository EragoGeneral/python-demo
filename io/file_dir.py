import os, sys

#print(os.name)

#查看当前目录的绝对路径
#print(os.path.abspath('.'))

p = os.path.join(os.path.abspath('.'), 'new')
#print(p)

#os.mkdir(p)

#os.rmdir(p)

f = os.path.join(os.path.abspath('.'), '1.txt')
#print(f)

t = os.path.split(f)
#print(t)

t1 = os.path.splitext(f)
#print(t1)



#当前目录下的所有目录
pp = 'G:\\mine'

for x in os.listdir(pp):
    if os.path.isdir(os.path.join(pp, x)):
        print(x)

#列出所有 .py文件
bb = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
#print(bb)







