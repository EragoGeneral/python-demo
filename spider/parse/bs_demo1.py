from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story </title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie -->< /a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3"> Tillie</a> ;
and they lived at the bottom of a well. </p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
#print(soup.title.string)

#选择元素
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)


# 提取信息
# 获取名称
print(soup.title.name)
# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['class'])
# 获取内容
print(soup.p.string)


html1 = """
<html><head><title>The Dormouse's story</title><head>
<body>
"""

soup = BeautifulSoup(html1, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)


html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
Once upon a time there were three little sisters ; and t heir names were
<a href="http://example.com/elsie" class="sister" id= "link1">
<span>Elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id=" link2">Lacie</a>
and
<a href＝"http://example.com/tillie" class=” sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class=" story"> .. . </p>
"""
# 使用contents
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
# 使用 children
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
# 使用 descendants
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 使用 parent 查找父节点
print(soup.a.parent)

# 使用 parents 查找祖父节点
print("使用 parents 查找祖父节点========================")
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

# 使用 sibling 查找兄弟节点
html2 = """
<html>
<body>
<p class="story">
        Once upon a time there were three little sisters ; and t heir names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
        Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        abd they lived at the bottom of a well.
</p>                        
"""

soup = BeautifulSoup(html2, 'lxml')
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next siblings', list(enumerate(soup.a.next_siblings)))
print('Prev siblings', list(enumerate(soup.a.previous_siblings)))


html3 = """
<html>
<body>
<p class="story">
Once upon a time there were three little sisters; and t heir nam es were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
class="sister" id="link2"> Lacie</a>
</p>
"""
soup = BeautifulSoup(html3, 'lxml')
print('Next Sibling: ')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])


html4 = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class ="element">Foo<li>
<li class="element">Bar<li>
<li class="element">Jay<li>
</ul>
<ul class="list list-small" id="list-2" name="elements">
<li class="element"> Foo<li>
<li class="element"> Bar<li>
</ul>
</div>
</div>
"""

soup = BeautifulSoup(html4, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))

print(soup.find_all(id="list-1"))
print(soup.find_all(class_="element"))

import re
html5 = '''
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a >
<a>Hello, this is a link, too</a>
<a>link</a>
</div>
</div>
'''
soup = BeautifulSoup(html5, 'lxml')
print(soup.find_all(text=re.compile('link')))

soup = BeautifulSoup(html4, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

# CSS 选择器
html6 = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">]ay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element"> Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html6, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

# 嵌套选择
print('======嵌套选择======')
for ul in soup.select('ul'):
    print(ul.select('li'))

# 获取属性
print('======获取属性======')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取文本
print('======获取文本======')
for li in soup.select('li'):
    print('Get Text: ', li.get_text())
    print('String: ', li.string)


