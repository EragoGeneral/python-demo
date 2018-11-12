import requests

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}

response = requests.get('https://www.taobao.com')
print(response.text)

