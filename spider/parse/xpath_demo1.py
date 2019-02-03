from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# 所有节点
result = html.xpath('//*')
print(result)

#指定节点
result = html.xpath('//li')
print(result)
print(result[0])

# 子节点    //ul//a 可以获取数组   而 //ul/a 则数据为空数组，因为 a 标签不是 ul 的子节点，是子孙节点
result = html.xpath('//li/a')
print(result)

# 父节点
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
# 用 parent:: 来获取父节点
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

#属性匹配
html1 = etree.parse('./test.html', etree.HTMLParser())
result = html1.xpath('//li[@class="item-0"]')
print(result)

#文本获取
result = html1.xpath('//li[@class="item-0"]/a/text()')
print(result)

result = html1.xpath('//li[@class="item-0"]//text()')
print(result)

# 属性获取
html2 = etree.parse('./test.html', etree.HTMLParser())
result = html2.xpath('//li/a/@href')
print(result)

# 属性多值匹配
text = '''<li class="li lii li-first" name="item" id="item"><a href="link.html">first time</a></li>'''
html = etree.HTML(text)
# 输出空， 因为 li 的 class 属性有两个值
result1 = html.xpath('//li[@class="li"]/a/text()')
print("result1", result1)
result2 = html.xpath('//li[contains(@class, "li")]/a/text()')
print("result2", result2)

# 多属性匹配
result = html.xpath('//li[contains(@class, "li") and @name = "item"]/a/text()')
print('result: ', result)


# 按序选择
content = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(content)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

# 节点轴选择
content = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html"><h1>second item</h1></a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(content)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[5]/child::a[@href="link5.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print("span: ", result)
result = html.xpath('//li[1]/following::*[3]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)

