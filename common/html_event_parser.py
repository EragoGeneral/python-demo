from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
from collections import defaultdict
import json

class PyWebHTMLParser(HTMLParser):
    def __init__(self):
        super(PyWebHTMLParser, self).__init__()
        self.sessions = []
        self.session = {}
        self.__enableFlag = False
        self.__flag = 0
        self.__title = ''

    def handle_starttag(self, name, attrs):
        if name == 'ul' and ('class','list-recent-events menu') in attrs:
            self.__enableFlag = True

        if self.__enableFlag:
            if name == 'li':
                self.__flag = 1

            if self.__flag == 1:
                if name == 'a':
                    self.__title = 'title'
                if name == 'time':
                    dictattrs = defaultdict(lambda: '', attrs)
                    self.session['date'] = dictattrs['datetime']
                if name == 'span':
                    self.__title = 'location'

    def handle_endtag(self, name):
        if self.__enableFlag:
            if name == 'ul':
                self.__enableFlag = False
            if name == 'li':
                self.__flag = 0
                self.sessions.append(self.session)
                self.session = {}

    def handle_data(self, data):   
        if self.__flag == 1 and len(self.__title) > 0:
            self.session[self.__title] = data
            self.__title = ''
    
    

URL = 'https://www.python.org/events/python-events/'
with request.urlopen(URL) as f:
    data = f.read()
	
parser = PyWebHTMLParser()
parser.feed(data.decode('utf-8'))
print(json.dumps(parser.sessions, indent=1))