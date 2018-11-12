import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)