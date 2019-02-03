from pyquery import PyQuery as pq


#字符串初始化
html = '''
<div>
<Ul>
<li class="item-O">first item</li>
<li class="item-1"><a href="link2.html">second item</a> </li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

doc = pq(html)
print(doc('li'))


# url初始化
import requests
#doc = pq(url = 'https://cuiqingcai.com')
#print(doc('title'))

#doc = pq(requests.get('https://cuiqingcai.com').text)
#print(doc('title'))


html2 = '''
<div id="container">
<ul class="list">
<li class="item-O">first item</li>
<li class="item-l"><a href="link2.html">second item</a></li >
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html2)
print(doc('#container .list li'))
print(type(doc('#container .list li')))


# 子节点 find()
print('======子节点 find()======')
doc = pq(html2)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

# 子节点 children()
print('======子节点 children()======')
lis = items.children('li')
print(type(lis))
print(lis)

lis = items.children('.active')
print(lis)

# 父节点   parent()
html3 = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-l"><a href="link2.html">second item</a></li >
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''

doc = pq(html3)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

# 祖先节点   parents()
print('======祖先节点   parents()======')
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)

parent = items.parents('.wrap')
print(parent)


# 兄弟节点   siblings()
print('======兄弟节点   siblings()======')
li = doc('.list .item-0.active')
print(li.siblings())
print(li.siblings('.item-0'))


# 遍历
li = doc('.item-0.active')
print(li)
print(str(li))

lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))

# 获取信息
print('======获取信息======')
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)

print('====遍历多元素属性====')
a = doc('a')
for item in a.items():
    print(item.attr('href'))

# 获取文本
a = doc('.item-0.active a')
print(a)
print(a.text())
li = doc('.item-0.active')
print(li.html())

li = doc('li')
print(li.html())
# html() 方法返回的是第一个li节点的内部HTML，而text()则返回了所有的li节点内部的纯文本，中间用一个空格分割开，即返回结果是一个字符串
print(li.text())
print(type(li.text()))

# 节点操作
print('======节点操作======')
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('.active')
print(li)


print('======attr, text, html======')
html4 = '''
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc = pq(html4)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>change item</span>')
print(li)

print('====remove()====')
html5 = '''
<div class="wrap">
    Hello, World
<p>This is a paragraph.</p>
</div>
'''
doc = pq(html5)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
print('======伪类选择器======')
html6 = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4 .html">fourth item</a></li>
<li class="item-0"><href="links.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html6)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)

li = doc('li:nth-child(4)')
print(li)

print('li:gt(2)')           #从0开始标识第一个元素
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n-1)')
print(li)
li = doc('li:contains(second)')
print(li)






