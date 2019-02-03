from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 执行 javascript
print("======执行 javascript======")
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 获取属性
print("======获取属性======")
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

# 获取文本
print("======获取文本======")
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

# 获取id, 位置, 标签名和大小
print("======获取id, 位置, 标签名和大小======")
input1 = browser.find_element_by_class_name('zu-top-add-question')
print(input1.id)
print(input1.location)
print(input1.tag_name)
print(input1.size)
browser.close()


# 切换 frame
print("======切换 frame======")
browser1 = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser1.get(url)
browser1.switch_to.frame('iframeResult')
try:
    logo = browser1.find_element_by_class_name('logo')
except NoSuchElementException:
    print('No LOGO')
browser1.switch_to.parent_frame()
logo = browser1.find_element_by_class_name('logo')
print(logo)
print(logo.text)
browser1.close()


# 显式等待
print("======显式等待======")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser2 = webdriver.Chrome()
browser2.get('https://www.taobao.com/')
wait = WebDriverWait(browser2, 10)
input2 = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input2, button2)
browser2.close()


# browser.execute_script('alert("To Bottom")')
# 前进和后退
print("======前进和后退======")
browser3 = webdriver.Chrome()
browser3.get('https://www.baidu.com/')
browser3.get('https://www.taobao.com/')
browser3.get('https://www.qq.com/')
browser3.back()
time.sleep(1)
browser3.forward()

# time.sleep(5)
browser3.close()


# Cookies
print("======Cookies======")
browser4 = webdriver.Chrome()
browser4.get('https://www.zhihu.com/explore')
print(browser4.get_cookies())
browser4.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser4.get_cookies())
browser4.delete_all_cookies()
print(browser4.get_cookies())
browser4.close()

# 选项卡管理
print("======选项卡管理======")
browser5 = webdriver.Chrome()
browser5.get('https://www.baidu.com/')
browser5.execute_script('window.open()')
print(browser5.window_handles)
browser5.switch_to.window(browser5.window_handles[1])
browser5.get('https://www.taobao.com/')
browser5.switch_to.window(browser5.window_handles[0])
browser5.get('https://www.qq.com/')
browser5.close()


browser6 = webdriver.Chrome()
try:
    browser6.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')

try:
    browser6.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser6.close()

