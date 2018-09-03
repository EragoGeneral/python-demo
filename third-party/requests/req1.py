import requests

r = requests.get('https://www.douban.com/') #豆瓣首页
print(r.status_code)
print(r.text)

r = requests.get('https://www.douban.com/search', params={'q':'python', 'cat':'1001'})
print(r.url)
print(r.encoding)
print(r.content)

