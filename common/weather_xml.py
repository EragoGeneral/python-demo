# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request


class WeatherSaxHandler(object):
    weather = {}
    forecastArr = []
	
    def weather_forecast(self, name, attrs):
        
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
            print('city: ' + self.weather['city'])
        
        if name == 'yweather:forecast':
            iteminfo = {}
            for k, v in attrs.items():
                if not k == 'xmlns:yweather':                    
                    iteminfo[k] = v
            self.forecastArr.append(iteminfo)            
            self.weather['forecast'] = self.forecastArr
            print('weather: {}, date: {}, low: {}, high: {}'.format(attrs['text'], attrs['date'], attrs['low'], attrs['high']))
        '''
		if name == 'yweather:forecast':
            self.weather['forecast'].append({
                'date': attrs['date'],
                'high': attrs['high'],
               'low' : attrs['low']
            })        
        '''
        

def parseXML(xml_str):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.weather_forecast
    parser.Parse(xml_str)
    return handler.weather


URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL) as f:
    data = f.read()
result = parseXML(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'



 