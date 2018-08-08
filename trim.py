    
def trim(s):	
    l=len(s)

    if len(s) == 0:
        return s
	
    if s[0] != ' ' and s[-1] != ' ':
        return s
    
    i=0	
    while i < len(s)-1 and  s[i] == ' ' :
        i = i + 1
    if s[0] == ' ':
        s = s[i:]    
    j=-1
    while len(s) > 0 and len(s) >= abs(j) and s[j] == ' ' :
        j = j - 1
	
    if s[-1] == ' ':
	    s = s[:j+1]	
    
    return s	

	

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

	