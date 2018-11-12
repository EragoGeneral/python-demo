import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2018-12-22 13:21'
# 这里没有必要重复写3个同样的正则表达式，可以借助 compile() 方法将正则表达式编译成一个正则表达式对象
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)

print(result1, result2, result3)

# 结果->> 2016-12-15  2016-12-17  2018-12-22


def greeting(name:str) -> str:
    return 'Hello ' + name


word = greeting('Bob')
print(word)

word1 = greeting(1)   #expect type str instead of int