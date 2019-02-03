from selenium import webdriver
import time

proxy = '118.190.94.224:9001'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
print(browser.page_source)
time.sleep(5)
browser.close()


service_args = [
    '--proxy=118.24.89.206:1080',
    '--proxy-type=http'
]
browser1 = webdriver.PhantomJS(service_args=service_args)
browser1.get('http://httpbin.org/get')
print(browser1.page_source)
time.sleep(3)
browser1.close()
