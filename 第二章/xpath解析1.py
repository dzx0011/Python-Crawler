from lxml import etree

xml="""
<html>
    <body>
        <p>data</p>
        <p>data1</p>
        <p>data2</p>
        <nick>
            <p>data3</p>
        </nick>
        <nick1>
            <p>data4</p>
        </nick1>
    </body>
    <name>flower</name>
</html>
"""
root=etree.XML(xml)


#调用lxml.etree.Element 类中的 xpath 方法。
result=root.xpath("/html")#/表示从根节点开始匹配,绝对路径
result1=root.xpath("/html/name/text()")#text()方法获取内部内容
print(result)
print(result1)

result2=root.xpath("/html/body//p/text()")#//表示任意，使用相对路径
print(result2)

result3=root.xpath("/html/body/*/p/text()")#*代表任意节点
print(result3)
