print('Hello Python!')

print('''line1
line2
line3''')

print(ord('A'))
print(chr(65))
print(ord('中'))
print(chr(25991))

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('显示中文')

print('Hi %s, your score is %d.' % ('Bart', 59))

print('%4d-%03d' % (3,1))
print('%.2f' % 3.141592654)

r = (85-72)/72
print('%.3f' % r)