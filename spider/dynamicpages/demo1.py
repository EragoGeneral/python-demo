from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://ip.zdaye.com/dayProxy/2018/11/1.html')
print(browser.current_url)

input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)

lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)

input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()

browser.close()

