from collections import namedtuple, deque, defaultdict, OrderedDict

# namedtuple
print('namedtuple demo...')
Point = namedtuple('Pt', ['x', 'y'])
p = Point(1, 2)
print(p.x, ' - ', p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1,1,2)
print(c.r)


#deque
print('deque demo...')
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)


#defaultdict
print('defaultdict demo...')
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


#OrderedDict
print('OrderedDict demo...')
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

od = OrderedDict()
od['x'] = 2
od['a'] = 3
od['z'] = 4
print(list(od.keys()))



