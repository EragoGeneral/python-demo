import xlrd
import xlwt
import time
import random
import string
from urllib import parse, request
import json
import hashlib

from datetime import date,datetime

def read_excel():

    with open('result.txt', 'a+') as f:
        f.writelines("{}{} {}{}".format('\n'*3, '自动测试时间开始:  ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '\n'))

    token = login()

    workbook = xlrd.open_workbook('urls.xlsx')
    #print(workbook.sheet_names()) # [u'sheet1', u'sheet2'])
	
    #print(len(workbook.sheet_names()))
 
    table = workbook.sheets()[1]
    rows = table.nrows
    #print(rows)

    ## temp variable
    deleteCommentId = 0
	
    header = {'product':'20001', 'X-UBT-DeviceId': '07D8530A-395B-404D-8E22-F3BA03A512EA', 'Content-Type': 'application/json', 'X-UBT-DeviceId': '07D8530A-395B-404D-8E22-F3BA03A512EA'}
    rowNum = 1
    while(rowNum < rows):
        name = table.cell(rowNum,0).value

        url = table.cell(rowNum,1).value
        method = table.cell(rowNum,2).value
        param = table.cell(rowNum, 4).value
        custom_header = table.cell(rowNum,3).value
        #param = data = { 'appSource': 'Jimu', 'appType': '1', 'pageNum': 1, 'pageSize': 50, 'requestKey': '1627A17B44F0B0B442C68C953A960EAE', 'requestTime': '9999999999', 'serviceVersion': '3.0.1', 'systemArea': 'CN', 'systemLanguage': 'zh-hans' }

        if url:
            sign = gen_sign()
            custom_header = json.loads(custom_header)
            for key in custom_header.keys():
                header[key] = custom_header[key]

            header["X-UBT-Sign"] = sign
            header["authorization"] = token
            #print(token)
            if method == 'get':
                req = request.Request(url, headers=header)
            else:
                if param:
                    data = json.loads(param)
                    data = bytes(json.dumps(data), 'utf8')
                else:
                    data = {}
                if url.find('/community/app/comment/delete') > 0:
                    url = url.format(str(deleteCommentId))
                    print(url)

                req = request.Request(url=url, headers=header, data=data, method=method.upper())

            status_code = 500
            try:

                res = request.urlopen(req)
                result_str = res.read().decode('utf-8')
                result = json.loads(result_str)
                #print(result)
                #print(result.get('token').get('token'))

                #print(res.getcode())
                status_code = res.getcode()
                if status_code == 200:
                    if url.find('community/app/comment/add') > 0:
                        deleteCommentId = result.get('id')
                        print(deleteCommentId)
            except:
                status_code = 500

            with open('result.txt', 'a+') as f:
                f.writelines("{} : {}{}".format(name, status_code, '\n'))

            '''
            result_str = res.read().decode('utf-8')
            result = json.loads(result_str)
            print(result)
            status = result.get('status')
            
            if status is True:
                print('OK!')
                #print(result)
            '''

        rowNum += 1

    with open('result.txt', 'a+') as f:
        f.writelines("{} {}{}".format('自动测试时间结束:  ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '\n'))

def gen_sign():
    '''
    x-ubt-deviceid	    07D8530A-395B-404D-8E22-F3BA03A512EA
    x-ubt-appid 		400010012 	de1571ede40b44c48217a041071729fa
                        400010011	a0a1dfa9a7d74d999f28b6b8ceaa0de3
    x-ubt-sign
    '''

    deviceId = '07D8530A-395B-404D-8E22-F3BA03A512EA'
    version = 'v2'
    randStr = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    now = str(int(time.time()))
    #print(int(now))
    mAppKey = 'de1571ede40b44c48217a041071729fa'
    #print(' '.join([deviceId, version, randStr, str(int(now)), mAppKey]))

    sign_key = ''.join([now, mAppKey, randStr, deviceId])
    #sign_key = '1551423081de1571ede40b44c48217a041071729faa8CtWUsJvl07D8530A-395B-404D-8E22-F3BA03A512EA'
    # now + mAppKey + randStr + deviceId
    #print(sign_key)
    md = hashlib.md5(sign_key.encode())
    sign = md.hexdigest()
    #print(' '.join([sign.upper(), now, randStr, version]))
    sign = ' '.join([sign.upper(), now, randStr, version])
    #print(sign)

    return sign


def login():
    token = gen_sign()
    print(token)
    data = {"account": "8613688990039", "accountType": "0", "appId": "400010012", "password": "328673579e5cf8ac62de13df4f30b530"}
    data = bytes(json.dumps(data), 'utf8')
    header = {'X-UBT-DeviceId': '07D8530A-395B-404D-8E22-F3BA03A512EA', 'product': '20001', 'Content-Type': 'application/json','X-UBT-AppId': '400010012', 'X-UBT-Sign': token}
    #header = { "Accept": "*/*", "X-UBT-Sign": token, "X-UBT-AppId": "400010012"}
    req = request.Request(url='http://10.10.20.72:8010/user-service-rest/v2/user/login', headers=header, data=data, method='PUT')
    res = request.urlopen(req)
    result_str = res.read().decode('utf-8')
    result = json.loads(result_str)
    #print(result)
    token = result.get('token').get('token')

    return token


if __name__ == '__main__':
    #login()
    read_excel()
    #gen_token()