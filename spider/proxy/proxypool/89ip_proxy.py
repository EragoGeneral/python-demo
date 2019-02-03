from utils import get_page
from pyquery import PyQuery as pq

urls = ['http://www.89ip.cn/index_{}.html'.format(page) for page in range(1, 10)]

for url in urls:
    html = get_page(url)
    doc = pq(html)
    trs = doc('.layui-table tbody tr').items()
    for tr in trs:
        ip = tr.find('td:nth-child(1)').text()
        port = tr.find('td:nth-child(2)').text()
        proxy = ':'.join([ip, port])
        print(proxy)

