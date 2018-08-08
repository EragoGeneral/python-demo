def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 5):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
	
f1, f2, f3, f4 = count()

print(f1())
print(f2())
print(f3())
print(f4())
print(f2())


def createCounter():
    count=[0]  
    def counter():   
        count[0]+=1  
        print(count[0],' access!')  
        return count[0]
    return counter 
    	

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')