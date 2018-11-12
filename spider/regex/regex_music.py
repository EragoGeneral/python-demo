import re

html = '''<div id="song-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# 提取 class为active 的 li 节点内部的超链接包含的歌手和歌名     <li.*?active.*?singer="(.*?)">(.*?)</a>
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)    # 由于代码有换行，所以这里第三个参数需要传入 re.S
if result:
     print(result.group(1), result.group(2))
# 结果->>    齐秦 往事随风

# 把active去掉
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)    # 由于代码有换行，所以这里第三个参数需要传入 re.S
if result:
     print(result.group(1), result.group(2))
# 结果->>    任贤齐 沧海一声笑

# 不加换行符匹配， 第一个li没有singer， 第二，三个li是换行
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)    # 由于代码有换行，所以这里第三个参数需要传入 re.S
if result:
     print(result.group(1), result.group(2))
# 结果->>    beyond 光辉岁月

# 获取所有 a节点的超链接、歌手和歌名， 可以将 search() 替换成 findall()
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(type(result))
for result in results:
    print(result)
    print(result[0], result[1], result[2])

'''
结果 ->>
<re.Match object; span=(292, 351), match='<li data-view="6"><a href="/4.mp3" singer="beyond>
<class 're.Match'>
('/2.mp3', '任贤齐', '沧海一声笑')
/2.mp3 任贤齐 沧海一声笑
('/3.mp3', '齐秦', '往事随风')
/3.mp3 齐秦 往事随风
('/4.mp3', 'beyond', '光辉岁月')
/4.mp3 beyond 光辉岁月
('/5.mp3', '陈慧琳', '记事本')
/5.mp3 陈慧琳 记事本
('/6.mp3', '邓丽君', '但愿人长久')
/6.mp3 邓丽君 但愿人长久
'''

# 获取所有li节点的歌名，直接用正则表达式来提取可能比较烦琐
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for result in results:
    print(result)    # 结果为元组，歌名在第二个元素  ('<a href="/2.mp3" singer="任贤齐">', '沧海一声笑', '</a>')
    print(result[1])

# 可以借助 sub() 将a 节点去掉，只留下文本
html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result)

