from io import StringIO
from io import BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('python!')

print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())
	
	
fb = BytesIO()
fb.write('中文'.encode('utf-8'))
print(fb.getvalue())

fb1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(fb1.read())
