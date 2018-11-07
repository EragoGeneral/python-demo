 # import urllib
from urllib import request

print("downloading with urllib")
url0 = 'http://media6.61info.cn/rbkd/course_new/2_3_C6C6251B06300001E384F820B38D1346/15s/2_3_1'   #第1课 168.ts
#'http://media6.61info.cn/rbkd/course_new/2_5_C6C62521FD80000166CA1C501D2F17EB/v2/2_5_1'       第2课 165.ts 
#'http://media6.61info.cn/rbkd/course_new/2_6_C6C62523A55000015D211240FB47CD90/v2/2_6_1'       第3课 160.ts

#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_30.ts		第4节
#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_31.ts

#http://media6.61info.cn/rbkd/course_new/2_7_C6C625256BB0000151408E005A2771E0/v1/2_7_1'			第5节 153.ts
#http://media6.61info.cn/rbkd/course_new/2_36_9E6737FFD33843CF943E495BF3740590/15s/2_36_1'		第6节 136.ts
#  url0 = 'http://media6.61info.cn/rbkd/course_new/2_8_C6C6252760000001F0AE3730B8AD1DE9/v2/2_8_1'     #第7课  162.ts
#http://media6.61info.cn/rbkd/course_new/2_10_C6CB2DF69A3000016EF9D3A0402415E2/v2/2_10_1'			第8节 167.ts
#http://media6.61info.cn/rbkd/course_new/2_11_C6CCF207B4300001919B17396F808D30/v1/2_11_1'    167.ts   第9节
#http://media6.61info.cn/rbkd/course_new/1_12_F865BD9BB064406FB3BBB87301D9B424/15s/1_12_1'    152.ts  第10节
#  url0 = 'http://media6.61info.cn/rbkd/course_new/2_12_C6CF34A21FC00001935713DC9F4012B3/15s/2_12_1'   #第11课     58

#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_3' 
#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_31.ts 
#第12节

#http://media6.61info.cn/rbkd/course_new/2_102_132462F1FD9D4FF8952F09F8DF206881/v1/2_102_2'   258.ts  第13节
#http://media6.61info.cn/rbkd/course_new/2_14_C6D3A02D38700001756A1C50A2F01F43/15s/2_14_1'    159.ts  第14节
#http://media6.61info.cn/rbkd/course_new/2_15_C6D5E124FAA000013DD16CB014D0FCB0/15s/2_15_1'    168.ts  第15节
#http://media6.61info.cn/rbkd/course_new/2_53_1B11A843D4E54B06816D8F2F670E3F47/15s/2_53_1'    158.ts  第16节
#http://media6.61info.cn/rbkd/course_new/2_54_07F68CBE26A040E59CF74C363174585D/15s/2_54_1'    154.ts  第17节
#http://media6.61info.cn/rbkd/course_new/2_20_C6E1426C85E00001437716C432951CE9/v2/2_20_1'     168.ts  第18节

#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_30.ts 
#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_31.ts 
#第19节

#http://media6.61info.cn/rbkd/course_new/2_21_C6E375BD6390000199C1FA6618C65BC0/15s/2_21_1'    162.ts  第20节
#http://media6.61info.cn/rbkd/course_new/2_22_C6E7EA7900600001BC4D1E9061321392/15s/2_22_1'    168.ts  第21节
#http://media6.61info.cn/rbkd/course_new/2_23_50D4E02AE30442FB9C56BC1BECF94B26/v2/2_23_1'     173.ts  第22节
#http://media6.61info.cn/rbkd/course_new/2_24_E905A195221142BBB6B31ACA10749C1E/v3/2_24_1'     145.ts  第23节

#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_3' 
#http://media6.61info.cn/rbkd/course_new/zhibo/zhibo_31.ts 
#第24节

#http://media6.61info.cn/rbkd/course_new/2_25_4A39783ADF454E70BE0EC59E6A9173B1/v2/2_25_1'     165.ts  第25节
#http://media6.61info.cn/rbkd/course_new/2_26_F01082A527844EB599307C17B27CA1E0/v2/2_26_1'     161.ts  第26节
#http://media6.61info.cn/rbkd/course_new/2_27_188670A418454721953A7663BF1AEDC5/v2/2_27_1'     171.ts  第27节
 
course = 1
for item in range(0, 69):
    file = str(item) + ".ts"
    url = url0 + file
    print(url)

    # 第一个参数网络地址；第二个参数 本地保存位置
    request.urlretrieve(url,"./videos/"+ str(course) +"/"+file)