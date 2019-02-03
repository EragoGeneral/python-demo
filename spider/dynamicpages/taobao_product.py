from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.PhantomJS()
wait = WebDriverWait(browser, 10)
KEYWORD = '外套'

def index_page(page):
    """
    抓取索引页
    :param page:    页码
    :return:
    """
    print('正在攫取第', page, '页')
    try:
        url = 'https://list.mogujie.com/s?q=' + quote(KEYWORD)
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        #browser = webdriver.Chrome(chrome_options = chrome_options)

        browser = webdriver.Chrome()
        #browser.execute_script("function(){Object.defineProperties(navigator,{ webdriver:{         get:() =&amp;gt; false        }    })}")

        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)
            )
        )
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_produts()
    except TimeoutException:
        index_page(page)


from pyquery import PyQuery as pq
def get_produts():
    """
    提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()

    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_to_mongo(result):
    """
    保存至MongoDB
    :param result:
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到MongoDB 失败')



MAX_PAGE = 100
def main():
    """
    遍历每一页
    :return:
    """
    for i in range(1, MAX_PAGE+1):
        index_page(i)
    #browser.close()


import time
import datetime
import sys
import os
import random

import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def common_click(driver,element_id,sleeptime=3):
    actions = ActionChains(driver)
    actions.move_to_element(element_id)
    actions.click(element_id)
    actions.perform()
    time.sleep(sleeptime)

def login_in(user,pwd):
    #open login page
    '''
    driver.get('https://s.taobao.com/search?q=' + quote(KEYWORD))
    time.sleep(3)
    sb=driver.find_element_by_class_name("login-switch")
    common_click(driver,sb)
    userbox=driver.find_element_by_id("TPL_username_1")
    pwdbox=driver.find_element_by_id("TPL_password_1")
    userbox.clear()
    userbox.send_keys(user)
    common_click(driver, pwdbox)
    pwdbox.send_keys(pwd)
    loadmore=driver.find_element_by_id("J_SubmitStatic")
    common_click(driver,loadmore)
    time.sleep(20)
    '''

if __name__ == '__main__':
    #DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.loadImages'] = True
    #DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "

    '''
    driver = webdriver.Chrome()
    driver.set_script_timeout(30)
    driver.set_page_load_timeout(30)    
    '''


    main()

