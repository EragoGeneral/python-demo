from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去
with create_query('Bob') as q:
    q.query()
	

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)
with tag('h1'):
    print('hello')
    print('world')

@contextmanager
def htmlelement(ele,link):
    print('<%s href="%s">' % (ele,link))
    yield
    print('</%s>' % ele)
with htmlelement('a', 'https://www.baidu.com'):
    print('click here!')


# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

'''
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
'''















