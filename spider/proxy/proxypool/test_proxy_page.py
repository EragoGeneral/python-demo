from utils import get_page
from pyquery import PyQuery as pq
import datetime
import re

print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

year = datetime.datetime.now().year
month = datetime.datetime.now().month


urls = ['http://ip.zdaye.com/dayProxy/{}/{}/{}.html'.format(year, month, page) for page in range(1, 2)]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'acw_tc=781bad2315435444611496993e6ce7bf85642ec493198c45be1265c7a25302; ASPSESSIONIDSASSBDAC=MMGLDNEAEFNPGFCABIFNNHGI; __51cke__=; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1543544422,1543544603; ASPSESSIONIDQATRADAD=KHCDEEFAFHJAKGIMPCFOEKDM; acw_sc__v3=5c00b06af885d04878ae2905159caa0ecca61997; __tins__16949115=%7B%22sid%22%3A%201543548632252%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201543550823394%7D; __51laig__=43; acw_sc__v2=NWMwMGIwODcyNDEyODJjZjY1YTg0ZDY4MDkyOWI0MTQ0NmQ3MGVlNg==; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1543549024',
    #'Host': 'http://ip.zdaye.com/dayProxy/2018/11/1.html',
    'Upgrade-Insecure-Requests': '1'
}

for url in urls:
    html = get_page(url, options=headers)
    #print(html.encode('iso-8859-1').decode('gbk'))
    if html:
        doc = pq(html)
        pers = doc('.ips').items()
        for per in pers:
            content = per.find('a')
            page = 'http://ip.zdaye.com' + content.attr('href')
            print(page)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Cookie': 'acw_tc=781bad2315435444611496993e6ce7bf85642ec493198c45be1265c7a25302; ASPSESSIONIDSASSBDAC=MMGLDNEAEFNPGFCABIFNNHGI; __51cke__=; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1543544422,1543544603; ASPSESSIONIDQATRADAD=KHCDEEFAFHJAKGIMPCFOEKDM; acw_sc__v3=5c00b06af885d04878ae2905159caa0ecca61997; acw_sc__v2=NWMwMGIwODcyNDEyODJjZjY1YTg0ZDY4MDkyOWI0MTQ0NmQ3MGVlNg==; ASPSESSIONIDQCRRCCBC=FMALELFAGLFOMPCBFANNKECO; __tins__16949115=%7B%22sid%22%3A%201543550644612%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201543553694905%7D; __51laig__=57; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1543551895',
                'Host': 'ip.zdaye.com',
                'Referer': 'http://ip.zdaye.com/dayProxy/2018/11/1.html',
                'content-type': 'charset=utf8',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }

            html = get_page(page, options=headers)
            content = html.encode('iso-8859-1').decode('gbk')
            doc = pq(content)
            print(doc)
            ips = doc('.cont')

            #result = re.search('<div.*?"cont"><br/>.*?@</div>', ips, re.S)
            #if result:
            #    print(result)
            print(ips)


