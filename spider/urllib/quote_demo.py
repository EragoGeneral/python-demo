from urllib.parse import quote, unquote

keyword = '壁纸'

url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

url = 'https://10.10.1.13/!/#%E7%9F%A5%E8%AF%86%E5%BA%93/view/head/test/%E6%9E%97%E6%B1%89%E9%94%90/%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3/DIY%E6%96%87%E4%BB%B6%E5%90%8C%E6%AD%A5-%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BE%E8%AE%A1%20v1.0.0.vsdx'
print(unquote(url))
