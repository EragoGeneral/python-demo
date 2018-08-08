def printChar(L):   
    L1=[] 
    for item in L:
        if isinstance(item, str):
            L1.append(item.lower())
    print(L1)		
    return L1

L2 = ['Hello', 'World', 18, 'Apple', None]
L = printChar(L2)
print(L2)

if L == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')