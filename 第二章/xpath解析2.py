from lxml import etree

root=etree.parse("xpath测试网页.html")
xml1=root.xpath("/html/body/ul/li[1]/a/text()")#获取到第一个内容
print(xml1)
xml2=root.xpath("/html/body/ul/li/a[@href='https://www.sogou.com/']/text()")#获取到第一个内容
print(xml2)

list_xml=root.xpath("/html/body/ul/li")#相对查找
for l in list_xml:
    ans=l.xpath("./a/text()")
    print(ans,end=' ')
    print(l.xpath("./a/@href"))#