import json
from urllib import request
import zlib
from balance import Balance
from mysqltools import MysqlTool
import time
from datetime import datetime
import traceback

#最赚钱
#url = 'https://xueqiu.com/service/tc/snowx/PAMID/cubes/rank?tid=PAMID&period=MONTH&page=1'

#热门组合
#url = 'https://xueqiu.com/cubes/discover/rank/cube/list.json?category=14&page=1&count=20'

#调仓历史
url = 'https://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH394419&count=20&page=1'
head = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.2.2029528961.1550207422; device_id=23208d27d4d3b383c4beba6764457777; s=e31p62ggm4; __utmz=1.1550207473.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bid=03e48b73be8844fdb834c87f05ba9774_js5lyxav; aliyungf_tc=AQAAAJ6Ci0YwMggAoqo+t9wcKToW1upR; _gid=GA1.2.1543907246.1550635702; Hm_lvt_1db88642e346389874251b5a1eded6e3=1550207422,1550635702; __utmc=1; xq_a_token.sig=knknlVAPG2nkQ9enLy6gnEylv5w; xq_r_token.sig=_SVEXsDz6FhNpFjXlGS8TPj_T7Q; u=1715473708; snbim_minify=true; __utma=1.2029528961.1550207422.1550799220.1550805407.14; __utmt=1; __utmb=1.3.10.1550805407; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1550805468; xq_a_token=0cf26bebb052fa1681993cfdac2f3a6770d0387f; xqat=0cf26bebb052fa1681993cfdac2f3a6770d0387f; xq_r_token=bd43932fe1dd029e00a1384d36a93c3f402d4b26; xq_is_login=1; xq_token_expire=Tue%20Mar%2019%202019%2011%3A19%3A27%20GMT%2B0800%20(CST)",
            "Host": "xueqiu.com",
            "Pragma": "no-cache",
            "Referer": "https://xueqiu.com/P/ZH394419",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

db = MysqlTool()

urls = ['https://xueqiu.com/service/tc/snowx/PAMID/cubes/rebalancing/history?cube_symbol=SP1010142&count=20&page=1',
        'https://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH394419&count=20&page=1',
        'https://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH1820238&count=20&page=1']

accounts = db.query_accounts()

for account in accounts:
    account_id = account[0]
    account_name = account[1]
    url = account[2]

    req = request.Request(url=url, headers=head)
    response = request.urlopen(req)
    #print(response.info().get('Content-Encoding'))
    decompressed_data = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)
    #print(*decompressed_data.decode('utf8').splitlines(True)[:10])

    data = json.loads(decompressed_data)
    histories = data.get('list')

    url = db.user_id()
    dd = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(1550714547))
    count = db.check_balance(None, 'SZ600000', dd)

    latestHistory = db.query_latest_history(account_id)
    if latestHistory:
        latestTime = latestHistory[0]
        latestTime = int(latestTime.timestamp())
    else:
        latestTime = 0

    if histories:
        for history in histories:
            status = history.get('status')
            if status == 'success':
                list = history.get('rebalancing_histories')
                if list:
                    for ele in list:
                        updated_at = int(ele.get('updated_at')/1000)
                        if latestTime < updated_at:
                            print(updated_at)
                            print(latestTime)
                            print('new records')
                            dd = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(updated_at))
                            balance = Balance(dd, ele.get('net_value'), ele.get('prev_net_value'), ele.get('prev_price'), ele.get('prev_target_volume'), ele.get('prev_target_weight'), ele.get('prev_volume'), ele.get('prev_weight'), ele.get('prev_weight_adjusted'), ele.get('price'), ele.get('proactive'), ele.get('rebalancing_id'), ele.get('stock_id'), ele.get('stock_name'), ele.get('stock_symbol'), ele.get('target_volume'), ele.get('target_weight'), updated_at, ele.get('volume'), ele.get('weight'))
                            balance.account_id = int(account_id)
                            # 生成balance 对象，进行数据库操作
                            balance.created_at = dd
                            db.save_balance(balance)
