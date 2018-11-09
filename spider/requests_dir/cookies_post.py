import requests

headers = {
    'host':'www.zhihu.com',
    'cookie':'d_c0="AFACPVxodQuPTsVTHcuacE5cuOSUKEV3dIo=|1489637655"; _zap=d6343712-c42f-4a46-a1c8-f47b187117db; q_c1=ccf78f4dd7af4061acf6b70d96236b0b|1504836053000|1489637655000; _xsrf=mTon4RqJ5zXOudZxmDaiWbuD2ruKNnNb; tst=r; q_c1=ccf78f4dd7af4061acf6b70d96236b0b|1541580347000|1489637655000; __utmc=51854390; tgw_l7_route=e0a07617c1a38385364125951b19eef8; __utma=51854390.131837410.1489637653.1541580306.1541586249.4; __utmb=51854390.0.10.1541586249; __utmz=51854390.1541586249.4.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; l_n_c=1; l_cap_id="Zjc2ZjU4Nzk2MGYzNGMyNWFhMWE2YzViMGMxYzg3ZmM=|1541586452|12265033c5205d1575412660eef87fc879b9c0fe"; r_cap_id="ZTNmYjkyM2NmZTkzNGRkMzk0Y2RiYjg0ZGFjNzQzYTg=|1541586452|1554b213ac0887eed15e29e0dc22f61df3dfd7b5"; cap_id="MDkyZDRlOThiMmI2NDMxMWIxNmEzZmNkZWY1ODdkY2M=|1541586452|06784b7e6d00bf483c4cbc2f40d8c60435b2ee4e"; n_c=1; capsion_ticket="2|1:0|10:1541586460|14:capsion_ticket|44:ZTk3MjUwZWFkZjkyNGU4YjhjY2MzNzBlMzg0ODRjNmI=|ef6bad7390a2e65edce95dda8e24e3089827b015c3e003ba2587ec6d00016bd7"; z_c0="2|1:0|10:1541586462|4:z_c0|92:Mi4xdzNVR0FBQUFBQUFBVUFJOVhHaDFDeVlBQUFCZ0FsVk5IZ3pRWEFCZEpOZUNmTnBsRG9nVWdQX29RVEpDU3kxSkRn|7be8f53d703eb436b518d101f8e71d7af396a1dbcee15248995f6c7c7c08af2b"; __utmv=51854390.100-1|2=registration_date=20121114=1^3=entry_date=20121114=1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

r = requests.get('https://www.zhihu.com/', headers=headers)
print(r.text)



cookies = 'd_c0="AFACPVxodQuPTsVTHcuacE5cuOSUKEV3dIo=|1489637655"; _zap=d6343712-c42f-4a46-a1c8-f47b187117db; q_c1=ccf78f4dd7af4061acf6b70d96236b0b|1504836053000|1489637655000; _xsrf=mTon4RqJ5zXOudZxmDaiWbuD2ruKNnNb; tst=r; q_c1=ccf78f4dd7af4061acf6b70d96236b0b|1541580347000|1489637655000; __utmc=51854390; tgw_l7_route=e0a07617c1a38385364125951b19eef8; __utma=51854390.131837410.1489637653.1541580306.1541586249.4; __utmb=51854390.0.10.1541586249; __utmz=51854390.1541586249.4.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; l_n_c=1; l_cap_id="Zjc2ZjU4Nzk2MGYzNGMyNWFhMWE2YzViMGMxYzg3ZmM=|1541586452|12265033c5205d1575412660eef87fc879b9c0fe"; r_cap_id="ZTNmYjkyM2NmZTkzNGRkMzk0Y2RiYjg0ZGFjNzQzYTg=|1541586452|1554b213ac0887eed15e29e0dc22f61df3dfd7b5"; cap_id="MDkyZDRlOThiMmI2NDMxMWIxNmEzZmNkZWY1ODdkY2M=|1541586452|06784b7e6d00bf483c4cbc2f40d8c60435b2ee4e"; n_c=1; capsion_ticket="2|1:0|10:1541586460|14:capsion_ticket|44:ZTk3MjUwZWFkZjkyNGU4YjhjY2MzNzBlMzg0ODRjNmI=|ef6bad7390a2e65edce95dda8e24e3089827b015c3e003ba2587ec6d00016bd7"; z_c0="2|1:0|10:1541586462|4:z_c0|92:Mi4xdzNVR0FBQUFBQUFBVUFJOVhHaDFDeVlBQUFCZ0FsVk5IZ3pRWEFCZEpOZUNmTnBsRG9nVWdQX29RVEpDU3kxSkRn|7be8f53d703eb436b518d101f8e71d7af396a1dbcee15248995f6c7c7c08af2b"; __utmv=51854390.100-1|2=registration_date=20121114=1^3=entry_date=20121114=1'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'host':'www.zhihu.com',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key,value)
r = requests.get('https://www.zhihu.com/', cookies = jar, headers=headers)
print(r.text)

