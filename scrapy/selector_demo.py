from scrapy import Selector

body = '<html><head><title>Hello World</title></head><body><span class="tag">Good</span>' \
       '<a class="baidu" href="http://www.baidu.com">百度</a>' \
       '<a class="sina" href="http://www.sina.com">新浪</a>' \
       '</body></html>'
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)

tag = selector.css('.tag::text').extract_first()
print(tag)

bd = selector.css('a.baidu::text').extract_first()
print(bd)

sa = selector.css('.sina::attr(href)').extract_first()
print(sa)