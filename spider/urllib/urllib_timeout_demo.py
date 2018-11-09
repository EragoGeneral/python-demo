import socket
import urllib.request
from urllib import error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except socket.timeout as e:
    print('TIME OUT')
