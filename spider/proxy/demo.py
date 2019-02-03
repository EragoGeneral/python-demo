from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '42.48.118.106:47040'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

