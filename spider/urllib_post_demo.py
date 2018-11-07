import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
bdata = response.read()
print(bdata)
print(bdata.decode('gb2312'))
