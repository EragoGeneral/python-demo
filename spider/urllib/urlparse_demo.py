from urllib.parse import urlparse, urlunparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

# ParseResult 实际上是一个元组
print(result.scheme, result[0], result.netloc, result[1], result.fragment, sep='\n')

# 构造 url 地址
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
