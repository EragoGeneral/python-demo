from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
# print(rp.mtime())
# print(rp.modified())
print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('Googlebot', 'https://www.jianshu.com/search?q=python&page=1&type=collections'))

# print(rp.can_fetch('GoodCrawler', 'http://example.webscraping.com'))
# print(rp.can_fetch('BadCrawler', 'http://example.webscraping.com'))
