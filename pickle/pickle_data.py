import pickle

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close

f = open('dump.txt', 'rb')
dd = pickle.load(f)
f.close()
print(d)


















