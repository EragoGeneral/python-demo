import functools


def now():
    print('2018-08-09')
	
f = now
#print(f())
#print(now.__name__)
#print(f.__name__)


def log(func):
    functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def new_now():
    print('2018-08-09 10:15')   
    
#print(now())
#print(new_now())


def log_text(text):
    def decorator(func):
        functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_text('excute')
def now_text():
    print('Now: 2018-08-09 10:30')

print(now_text())

aa = log_text('excute')(now_text)
print(aa())