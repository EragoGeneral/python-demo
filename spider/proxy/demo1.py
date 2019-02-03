import requests

proxy = '118.190.94.224:9001'
proxies = {
    'http' : 'http://' + proxy
}

try:
    response = requests.get('http://httpbin.org/get', proxies = proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
