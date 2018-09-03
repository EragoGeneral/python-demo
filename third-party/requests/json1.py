import requests

## https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid = 2151330&format=json
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())