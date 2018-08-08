names = ['Michael', 'Bob', 'Tracy']
print(names)
for name in names:
    print(name)
	
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)	

print(list(range(5)))	

sum1 = 0
n = 99
while n > 0:
    sum1 = sum1 + n
    n = n - 2
print(sum1)	

# 字典
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print(d['Michael'])
d['Adam']=67
print(d['Adam'])
d['Jack']=88
print(d['Jack'])


# print(d['Thomas'])
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))

d.pop('Bob')
print(d)

key = [1,2,3]
# d[key] = 'a list'    error occurs

s = set([1,2,3,1,2,3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1,2,3])
s2 = set([1,2,4])
print(s1 & s2)
print(s1 | s2)

t = (1,2,3)
s.add(t)
print(s)

t1 = (1, [2, 3])
#  s.add(t1)     error occurs
#  print(s)

items = [x*x for x in range(1,11)]
print(items)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print (k, '=', v)

	
iter = iter([1,2,3,4,5])
while True:
    try:
        x = next(iter)
        print(x)
    except StopIteration:
        break	
	


