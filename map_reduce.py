from functools import reduce

def fn(x,y):
    return x*10 + y
	
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]

n = reduce(fn, map(char2num, '45332'))
print(n)


def normalize(name):
    f = name[0].upper()
    o = name[1:].lower()
    return f + o

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



def prod(L):
    def aa(x,y):
        return x*y
    return reduce(aa, L)
	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')