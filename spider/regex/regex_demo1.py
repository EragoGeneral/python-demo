import re

content = 'Hello 1234567 223 998 World_This is aRegex Demo'
result = re.match('^Hello\s(\d+)\s(\d+)\s(\d+)\sWorld', content)

print(result)

# group() 与 group(n) 之前的区别：前者会输出完整的匹配结果， 后者会输出第一个被（）包围的匹配结果 从 group(1) 开始
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))
print(result.span())

