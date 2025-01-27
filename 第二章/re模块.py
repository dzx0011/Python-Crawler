import re
#返回值是列表
#由于Python的字符串本身也用\转义,推荐使用r前缀，转换成python字符串，不用考虑转义字符

#findall匹配字符串所有符合正则的内容
lst=re.findall(r"\d{4}\-\d{2}\-\d{2}","我的生日是:2005-10-28,它的生日是:2000-10-10")
print(lst)

#finditer匹配字符串中所有内容[返回的是迭代器]
it=re.finditer(r"\d{4}\-\d{2}\-\d{2}","我的生日是:2005-10-28,它的生日是:2000-10-10")
for i in it:
    #匹配结果是一个 re.Match 对象，而匹配内容需要通过 group() 方法来提取。
    print(i.group())

#返回第一个结果，也是$ re.Match $对
s=re.search(r"\d{4}\-\d{2}\-\d{2}","我的生日是:2005-10-28,它的生日是:2000-10-10")
print(s.group())


#默认从开头开始匹配
m=re.match(r"\d{4}\-\d{2}\-\d{2}","我的生日是:2005-10-28,它的生日是:2000-10-10")
print(m)

#预加载,创建正则表达式对象
com=re.compile(r"\d{4}\-\d{2}\-\d{2}")
res=com.finditer("我的生日是:2005-10-28,它的生日是:2000-10-10")
res1=com.findall("它的生日是:2000-10-10")
for i in res:
    print(i.group())
print(res1)


