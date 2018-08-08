def findMinAndMax(L):
    print(L)
    if L == []:
        return (None, None)
    
    min_val = L[0]
    max_val = L[0]	
    for item in L:
        if item >= max_val:
            max_val = item
        if item <= min_val:
            min_val = item		
    return (min_val, max_val)
		
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')	