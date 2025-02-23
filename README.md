# 一.初始

## 渲染方式

### 服务器渲染

在服务器将数据和$html$整合，统一返回浏览器

### 客户端渲染

第一次请求只要一个$html$骨架，第二次请求拿到数据，进行数据展示，在源代码中看不到数据



## HTTP协议

### 请求

#### 1.请求行

请求方式(request)(post(你需要向服务器提交数据，并且数据会修改服务器状态)/get(获取数据而不修改服务器数据))      请求$url$    协议

#### 2.请求头

服务器附加信息

##### 请求头重要内容

1.$User\_Agent$请求载体的身份标识(用什么发送的请求)

2.$Referer$防盗链：请求从哪个页面而来

3.$cookie$：本地字符串数据信息(用户登录信息，反爬$token$)

#### 3.请求体

请求参数

### 响应

#### 1.状态行

协议 状态码 200,404,500,302

#### 2.响应头(header)

放在客户端的附加信息

##### 响应头重要内容

1.$cookie$：本地字符串数据信息(用户登录信息，反爬的token)

2.各种字符串(一般是token字样)

#### 3.响应体

真正返回客户端的内容$HTML，json$等

## 简单的代码

### 1. get

==$url$中的参数在？后，会自动转换成字符串参数方便操作(query string parameters)==

$python$默认的$user-agent$是`'User-Agent': 'python-requests/2.31.0'`

```python
import requests
query=input("请输入一个你要搜索的内容：")
url=f'https://www.sogou.com/web?query={query}'
#处理一个小反爬
header={
"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
#地址栏使用get提交

resp=requests.get(url,headers=header)
#text响应体的字符串形式
print(resp.text)
resp.close()#关闭respose，防止请求次数过多
```

### 2. post

==post请求发送的数据在请求体中，需要放在字典中，通过data参数传递==

```python
import requests
url="https://fanyi.baidu.com/sug"

f_str=input("请输入部分单词:")
dat={
    "kw":f_str
}
#post请求发送的数据需要放在字典中，通过data参数传递
resp=requests.post(url,data=dat)
print(resp.json())#服务其返回内容直接处理成json，方便你对返回的数据进行处理。
resp.close()#关闭respose，防止请求次数过多
```

## 抓包的过滤

1.$XHL$：许多 SPA（单页应用程序）会大量使用 $XHR$ 请求来加载数据，避免重新加载整个页面。许多网页通过 $XHR $进行**数据传输**，尤其是$ JSON $格式的数据，如获取文章列表、评论、用户信息等。

2.$CSS$：**层叠样式表**。是一种用于描述 HTML 或 XML 文档的外观和格式的样式表语言。它控制页面的布局、字体、颜色、大小、间距等视觉效果。

3.$JS$：$JS$ 是 **JavaScript** 的缩写，是一种广泛使用的编程语言，主要用于为网页添加交互性。

## 小例子：获取豆瓣前100剧情片

==客户端渲染==：使用$API$接口获取结构化的$JSON$数据 

```python
import requests
url="https://movie.douban.com/j/chart/top_list"

parame={
"type":"11",
"interval_id": "100:90",
"action": None,
"start": "0",
"limit": "100",
}
header={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

resp=requests.get(url,params=parame,headers=header)
answer_dir=resp.json()
for i in range(100):
    print(answer_dir[i]['rank'],answer_dir[i]['title'],answer_dir[i]['rating'])

resp.close()#关闭respose，防止请求次数过多
```



# 二.数据解析和提取

## 1.$RE$解析

### 正则表达式

#### 元字符

##### 1.边界

``` 
^     匹配字符串的开始,^\d\d必须从两个数字字符开始
$     匹配字符串的末尾
\b    匹配一个单词的边界，也就是指单词和空格间的位置“er\b”可以匹配“never”中的“er”，但不能匹配“verb”中       的“er”；“\b1_”可以匹配“1_23”中的“1_”，但不能匹配“21_3”中的“1_”。
```

##### 2.量词

```
*     匹配前面的子表达式任意次。例如，zo*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于{0,}。
+     匹配前面的子表达式一次或多次(大于等于1次）。“zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。等价{1,}。
?     当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。
{n}   n是一个非负整数。匹配确定的n次。例如，“o{2}”不能匹配“Bob”中的“o”，但是能匹配“food”中的两个o。
{n,}  n是一个非负整数。至少匹配n次。例如，“o{2,}”不能匹配“Bob”中的“o”，但能匹配“foooood”中的所有o。
{n,m} m和n均为非负整数，其中n<=m。最少匹配n次且最多匹配m次。例如，“o{1,3}”将匹配“fooooood”中的前三个o       为一组，后三个o为一组。“o{0,1}”等价于“o?”。请注意在逗号和两个数之间不能有空格。
```

##### 3.字符

```
.     匹配除了"\n"和"\r"之外的任何字符，要匹配包括"\n"和"\r"在内的任何字符，请使用像“[\s\S]”的模式。
\w    匹配包括下划线的任何单词字符
\s    匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。
\d    匹配一个数字字符。等价于[0-9]
x|y   匹配x或y。例如，“z|food”能匹配“z”或“food”(此处请谨慎)。“[z|f]ood”则匹配“zood”或“food”。
()    匹配括号内的表达式，组
[xyz] 字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”。 
[^xyz] 负值字符集合。匹配未包含的任意字符。例如，“[^abc]”可以匹配“plain”中的“plin”任一字符。
[a-z] 字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
```

\W,\S,\D代表对应的反义

#### 贪婪匹配和懒惰匹配

```
.*  贪婪匹配
.*? 懒惰匹配(?起到回溯作用)
注：以上两种在未使用re.S时都不匹配\n
```

### $RE$模块

$findall(pattern,str)$匹配字符串所有符合正则的内容，返回列表

$finditer(pattern,str)$匹配字符串中所有内容[返回的是迭代器],匹配结果是一个` re.Match `对象

$search(pattern,str)$返回==第一个==结果，也是`re.Match `对象，同样需要`group`方法提取字符串

$match(pattern,str)$默认从==字符串首==开始匹配，相当于`^pattern`

$compile(pattern)$将正则表达式编译为一个正则表达式对象，预加载提高匹配效率

### 例1：获取豆瓣评分前250的电影

==服务器渲染==：使用正则表达式在网页源代码中获取

将结果储存到$csv$文件中，方便后续使用$panda$进行数据分析操作

flags参数`re.S`让.可以代替\n

```python
import requests
import re
import time
import csv

url="https://movie.douban.com/top250"
start=0

header={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


for j in range(10):
    para={
    "start":str(start),
    "filter":""
    }

  
    resp=requests.get(url,headers=header,params=para)
    
    time.sleep(1)  # 每次请求之间等待1秒防止被短期封锁
    
    #re.S让.可以代替\n
    com=re.compile(r'<li>.*?<div class="item">.*?<em class="">(?P<order>.*?)</em>.*?<span class="title">(?P<movieTitle>.*?)</span>.*?<p class="">.*?<br>[\s]+(?P<year>.*?)&nbsp;.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?</li>',flags=re.S)

    ans_string= resp.text
    result=com.finditer(ans_string)

  # 使用with open语句自动管理文件打开和关闭,newline防止结果换行
    with open("data.csv", mode="a", encoding="utf-8", newline="") as f:
        # 创建csvwriter对象
        csvwriter = csv.writer(f)

        # 遍历结果并写入CSV
        for i in result:
            print(i.group("order"), i.group("movieTitle"), i.group("year"), i.group("score"))
            # 将组转化成字典groupdict
            resDic = i.groupdict()

            # 使用writerow逐行写入
            csvwriter.writerow(resDic.values())
    start=start+25

resp.close()
```

### 例2：获取子页面的下载地址

==网页显示的是经过渲染的结果，可以使用正则["\\']==超链接内使用'

group()函数默认为0，代表全体，填捕获组的序号或者填写自定义名称捕获指定组

==注意对子网站的编码方式的更改==

记得关闭HTTP响应对象（尤其在子循环中）

```python
import requests
import re
import time

url="https://www.dytt89.com/"

head={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

resp=requests.get(url,headers=head)
resp.encoding="gb2312"


#定位到指定的栏中
obj1=re.compile(r'<span style="float:left;">2024必看热片</span>.*?<ul>(?P<movieDetail>.*?)</ul>',flags=re.S)


#网页显示的是经过渲染的结果，"可能是'可以使用正则["\']
obj2=re.compile(r"<li><a href=[\"'](?P<href>.*?)[\"'] title=[\"'](?P<title>.*?)[\"']>.*?</li>",flags=re.S)

obj3 = re.compile(r'<div id="downlist".*?<a href="(?P<aurl>.*?)".*?</div>', flags=re.S)




result1=obj1.finditer(resp.text)
resp.close()
for i in result1: 
    
    result2=obj2.finditer(i.group('movieDetail'))
    #子网站的参数
    sub_head={
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": url
    }

    for j in result2:
        #在该层for循环中，我们获取到了每个超链接的url
        #strip() 去除的是字符串首尾的字符
        url_t=url+j.group(1).strip('/')

        resp_sub=requests.get(url_t,headers=sub_head)
        #同样记得处理编码(重)
        resp_sub.encoding="gb2312"
        
        #使用search接受一个对象
        result3=obj3.search(resp_sub.text)
        #记得关闭HTTP响应对象
        resp_sub.close()
        
        with open("downloadURL.txt",mode='a',encoding='gbk') as f:
            f.write(result3.group('aurl')+'\n')
        

```

出现问题，网络波动导致无法彻底进行

优化

```python
import requests
import re
import time

url = "https://www.dytt89.com/"

head = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# 正则表达式对象
obj1 = re.compile(r'<span style="float:left;">2024必看热片</span>.*?<ul>(?P<movieDetail>.*?)</ul>', flags=re.S)
obj2 = re.compile(r"<li><a href=[\"'](?P<href>.*?)[\"'] title=[\"'](?P<title>.*?)[\"']>.*?</li>", flags=re.S)
obj3 = re.compile(r'<div id="downlist".*?<a href="(?P<aurl>.*?)".*?</div>', flags=re.S)

try:
    # 获取主页面
    resp = requests.get(url, headers=head, timeout=5)
    resp.encoding = "gb2312"
    result1 = obj1.finditer(resp.text)
    resp.close()
    
    # 遍历每个电影的详情链接
    for i in result1:
        result2 = obj2.finditer(i.group('movieDetail'))
        
        sub_head = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Referer": url
        }

        for j in result2:
            url_t = url + j.group('href').strip('/')
            print(f"正在处理链接：{url_t}")

            # 尝试访问子页面，重试机制
            retries = 3  # 重试次数
            while retries > 0:
                try:
                    resp_sub = requests.get(url_t, headers=sub_head, timeout=5)
                    resp_sub.encoding = "gb2312"
                    result3 = obj3.search(resp_sub.text)
                    resp_sub.close()

                    if result3:
                        download_url = result3.group('aurl')
                        print(f"获取到下载链接：{download_url}")

                        # 逐行写入文件
                        with open("downloadURL.txt", mode='a', encoding='gbk') as f:
                            f.write(download_url + '\n')
                    else:
                        print(f"未找到下载链接：{url_t}")
                    
                    break  # 成功时退出重试
                except Exception as e:
                    retries -= 1
                    print(f"访问失败，重试中... 剩余尝试次数：{retries}")
                    time.sleep(2)  # 等待2秒后重试
            
            if retries == 0:
                print(f"最终失败，跳过链接：{url_t}")

except Exception as e:
    print(f"程序运行时发生错误: {e}")

```



### 例3：$post$爬取菜价(POST的简单回顾)

持续从网络中获取表格不同页码上的动态数据

```python
import requests
import csv
import time
from bs4 import BeautifulSoup

url="http://www.xinfadi.com.cn/getPriceData.html"



#i代表页码
for i in range(1,11):
    data_={
        "current":i,
        "limit":20
    }
    header={
        "referer":"http://www.xinfadi.com.cn/priceDetail.html",
        "accept-encoding":"gzip, deflate",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
  
    # 尝试访问子页面，重试机制
    retries=3  # 重试次数
    while retries>0:  
        try:
            resp=requests.post(url,data=data_,headers=header)
            js=resp.json()
            with open("./菜价.csv",mode="a",encoding="utf-8",newline='') as f:
            #创建csv对象,根据文档
                csvwriter=csv.writer(f)
                for j in range(20):
                    #csvwriter.writerow() 时，传递的参数需要是一个可迭代的对象
                    csvwriter.writerow([js["list"][j]["prodName"],js["list"][j]["lowPrice"],js["list"][j]["avgPrice"],js["list"][j]["highPrice"],js["list"][j]["place"]])
            resp.close()

            break  
            #尝试成功退出循环
        except Exception as e:
            retries-=1
            print(f"第{i}页的第{3-retries}次尝试失败，还剩{retries}次尝试")
            time.sleep(1)
    time.sleep(0.1)
```



## 2.$BS4$解析

### $html$语法（超文本）

```
标签，属性，属性值   <标签 属性=“属性值”>内容</标签>   或自带闭合<标签 />
h1:一级标题
h2:二级标题
```

通过标签值获取到内容

==**使用范围：静态加载的数据**==

### 步骤

①.创建$bs$对象解析数据
默认参数：markup，解析内容；feature，解析器($'html.parser'、'lxml'、'html5lib'$)；builder，这个参数用于选择文档树的构建

②.从$bs$对象中查找数据

$find$(标签，属性=值)  find('标签')['属性'']返回第一个值,$findAll$(标签，属性=值)返回列表。==$findAll$中string参数用于配合正则，或者传入函数通过函数逻辑筛选符合条件的字符串或者类型==

$select$(标签)可以通过$css$的选择器形式选择标签；或$select$(“标签[属性]”))$select$(“标签[属性=值]”))；又或者$select$("标签 标签")使用空格分隔表示层级选择器。      返回列表

使用$find$,$find\_all$获取到的是$tag$类型的对象和列表，使用==$tag.text\ or\ tag.gettext()$获取相应文本内容，$tag.get('属性')$==获取对应的值。其中后者可以加上更多参数进行优化输出如：strip=True去除多余的空格和换行符。

 `csv.writer` 传入一个可迭代对象（列表，元组），若存在键值对自动写入键

 `csv.DictWriter` 处理字典类型数据的。它接收一个字典，其中字典的键将成为 $CSV$文件的列名，字典的值将写入对应的列中。

### 例1：获取菜价等信息

```python
from bs4 import BeautifulSoup
import requests
import re
import csv

url="http://www.shucai123.com/price/"

header={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    
}

resp=requests.get(url,headers=header)
#将页面源代码交给beatifulsoup


#解析数据
#默认参数：markup，解析内容；feature，解析器('html.parser'、'lxml'、'html5lib')；builder，这个参数用于选择文档树的构建
bs=BeautifulSoup(resp.text,'html.parser')#构造bs对象，指定html.parser解析器


#从tag对象中查找数据
#find find_all select标签

#dat=bs.find("div",class_="mw")两种均可
table=bs.find("table",attrs={#class是关键字加上class_进行区分
    "class":"bjtbl"
})#查找后仍然是bs对象

#创建列表对象
vegetableInfo=[]

comPrice=re.compile(r'：(?P<price>.*?)元/斤')
comType=re.compile(r'(?P<type>.*?)：')
comMarket=re.compile(r'元/斤(?P<market>.*)')#使用贪婪匹配

if table:
    data=table.find_all("tr")[1:]#tr:行,屏蔽掉表头
    for trs in data:
        element=trs.find_all("td")
        date=element[0].get_text(strip=True)
        location=element[1].get_text(strip=True)
        category=element[2].get_text(strip=True)
        details=element[3].get_text(strip=True)
        type=comType.findall(details)
        price=comPrice.findall(details)
        market=comMarket.findall(details)
        contact=element[4].get_text(strip=True)

        vegetableInfo.append({
            "date":date,
            "location":location,
            "category":category,
            "type":type[0],
            "price":price[0]+"元/斤",
            "market":market[0],
            "contact":contact
        })

for i in vegetableInfo:
    print(i)


with open("vegetable_detail.csv","a",newline='',encoding="utf-8") as f:
    csvwriter=csv.DictWriter(f,fieldnames=vegetableInfo[0].keys())#获取字典的键
    csvwriter.writerows(vegetableInfo)

resp.close()  


```

### 例2：使用$bs4$爬取壁纸

`.content` 返回的是原始的二进制数据，非常适合用于保存图片、视频等二进制文件。即使 URL 是图片本身，`.content` 依然适用。

```python
import requests
import re
from bs4 import BeautifulSoup,Comment
import os

url="https://dailybing.com/"

resp=requests.get(url)

bs=BeautifulSoup(resp.text,'html.parser')

#第一次定位到图片的整体列表上
tag1=bs.findAll("div",class_="image-dock")

#第二次对应到a标签上
tag2=tag1[0].findAll("a")
resp.close()
for a in tag2:
    #tag.get获取属性对应的值
    tagURL=a.get('href')


    url=tagURL
    resp=requests.get(url)
    bs=BeautifulSoup(resp.text,'html.parser')
    tag1=bs.findAll('main',class_='shadow',)
    tag2=tag1[0].findAll('div',class_="tool-nav shadow")
    #findAll中string参数用于配合正则，传入函数通过函数逻辑筛选符合条件的字符串或者类型
    comments=tag2[0].findAll(string=lambda text:isinstance(text,Comment))

    #获取标题
    tag3=tag1[0].findAll('div',class_="image-wrap")
    titletag=tag3[0].findAll('img')
    title=titletag[0].get('data-title')
    
    #接着使用正则从注释中获取到下载地址
    com=re.compile(r'href="(?P<durl>.*?)"')
    downLoadURL=com.findall(comments[0])
    print(downLoadURL[0])
    resp.close()
    
    #写入文件
    save_folder="./下载壁纸"#文件夹路径
    file_name=title+".png" #图片名称
    save_path=os.path.join(save_folder,file_name)#组合完整路径

    resp=requests.get(downLoadURL[0])

    if resp.status_code==200:
        with open(save_path,'wb')as f:
            f.write(resp.content)
        print("已下载")
    else:
        print("下载失败，状态码为"+resp.status_code)

    
```



## 3.$Xpath$解析

`xpath`，在`XML`文档中搜索内容的一门语言，`html` 是 `xml`的子集。

==类似于树的结构，按照节点的关系进行查找==。

### 步骤

①.==`etree.XML(text) `==是 `lxml.etree` 中的一个函数，用于解析 XML 格式的字符串并返回其根节点，`lxml.etree.element`类型

`etree.parse(sourse)`，读取文件返回根节点

②.调用`lxml.etree.Element` 类中的 `xpath` 方法，使用==`xpath`表达式定位==来返回匹配结果。

### $Xpath$表达式定位

`xpath` 使用路径表达式在 `HTML/XML`文档中选取节点

| 表达式                       | 描述                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| /                            | 从根节点选取（取子节点）绝对路径                             |
| //                           | 任意节点，不考虑位置（取子孙节点）相对路径                   |
| .                            | 选取当前节点                                                 |
| …                            | 选取当前节点的父节点                                         |
| @                            | 选取属性                                                     |
| contain(@属性，“包含的内容”) | 模糊查询                                                     |
| text()                       | 文本内容                                                     |
| *                            | 任意节点                                                     |
| []                           | `[1]` 选择第一个匹配的元素。 `[condition  @XXX="xxx"]` 选择满足条件的元素。 |

#### 程序1

```python
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

```

![image-20250127164630013](C:\Users\17677\AppData\Roaming\Typora\typora-user-images\image-20250127164630013.png)

#### 程序2

```python
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
    print(l.xpath("./a/@href"))#获取属性值
```

![image-20250127191338818](C:\Users\17677\AppData\Roaming\Typora\typora-user-images\image-20250127191338818.png)

#### tip

浏览器选择元素后右键即可获取$xpath$

### 例1：$Xpath$爬取商品信息

在 `XPath` 中，尽量使用相对路径来定位元素。相对路径更具适应性，在页面结构发生小的变化时，可能仍能正常工作。

动态渲染的数据无法直接获取得到

```python
from lxml import etree
import requests
import csv

url="https://www.zbj.com/fw/?k=LOGO%E8%AE%BE%E8%AE%A1&fr=pc_zbj_v2022-homepage"
resp=requests.get(url)

#获取div
root=etree.HTML(resp.text)
divs=root.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')


with open("xpath爬取商品信息.csv",mode='a',encoding="utf-8",newline='')as f:
    csvwriter=csv.writer(f)
    first_row=["price","label","company_name"]
    csvwriter.writerow(first_row)

#针对一些动态渲染的数据无法直接获取得到
for div in divs:
    try:
        price=div.xpath('./div/div[3]/div[1]/span/text()')[0].strip('¥')
        label="logo设计".join(div.xpath('./div/div[3]/div[2]/a/span/text()'))#join连接
        company_name=div.xpath('./div/div[5]/div/div/div/text()')[0]
        print(price,label,company_name)
        with open("xpath爬取商品信息.csv",mode='a',encoding="utf-8")as f:
            f.write(price+','+label+','+company_name+'\n') 
    except:
        continue
resp.close()

```

# 三.requests进阶

模拟浏览器登录-处理cookie；防盗链处理；代理

## 1.处理cookie

登录获取`cookie`，带着`cookie`再获得`url`

启用断点，保存日志

```python
import requests


#session会话，cookie不丢失
session=requests.session()
header={
    "origin":"https://passport.17k.com",
    "referer":"https://passport.17k.com/login/",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

data={
    "loginName": "18250927959",
    "password": "chenhezhuma1"
}

url="https://passport.17k.com/ck/user/login"
resp=session.post(url,data=data,headers=header)
print(resp.cookies)


#2.直接获取到cookie给程序
url="https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"
cookie="GUID=344bac05-ed7a-4a04-9648-8f897ff38af9; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F12%252F12%252F30%252F103983012.jpg-88x88%253Fv%253D1738486407000%26id%3D103983012%26nickname%3Dbilibili111%26e%3D1754040296%26s%3D5d9fd296288f79ab; tfstk=gj7oZlgIGg-7fm6tet87fVct-yqvNbTBc93ppepU0KJXp79Je6Wht1-ea4WRmpXVnL8pyaUhxK8yAgppepYhOOVYBPUON_TBbReTWFSYUsY6abJrpnk2TeAPmynay_TB8-E1OxMPNOrjatFH8SY2tBuy82We0IJXOBkyT4PcgK9qzBRr8j52_Coy8eWFgSAB3QkseD9GFOQ4nmoA3EjfdZAkqd50fq0qfQk9L_Jo82JkZ3mcaK0E8ZjYWhdBUlGvdUp5NQXQ54TyxM7Juay48FS1nwxwSkFW7a1FfM5jEWvPMT_MzN2oyIKHEi7ymXueuEIybMXuE09P2tx6gnl35IB93__PmWMVaOpkzI-Y75f2YiQWfaeqrFS1wUIFQ-nJUGAF47nqbIfjRIPdoDiB4IODBq1JkCdXpKDYiSm_u3RXNrV0iDiB4IODBSVmfr-yGQac.; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103983012%22%2C%22%24device_id%22%3A%22194c5dc67b5fc6-0f7f26b4b5a356-26011b51-1821369-194c5dc67b61e32%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22344bac05-ed7a-4a04-9648-8f897ff38af9%22%7D; acw_sc__v2=679f506d879617ea2c360070b7bd0701de6f36cc; Hm_lvt_9793f42b498361373512340937deb2a0=1738486344,1738494067; HMACCOUNT=BE7DBABC5B2E8C13; ssxmod_itna=YqRx2C0QoCqrDXKDHD0Q5iqdx0xiq2HPG=aeQK8Ko8DlODWqeGzDAxn40iDtxhVETPoaKeLbj7Ut98TPK03xcoWr3LB87KDHxY=DUpYuGhD4+5GwD0eG+DD4DWDmnHDnxAQDjxGPyn2v5CDYPDEB5DRcPDu=AhDGc1Uh9hDeKD0OTHDQI+2axDBahAaWKqpahhDiWH5zvIcpifK7GkD7v+DlaQBFhkFIMUanHf2tdhUGKDXpQDvpHmnEge2Zvze325UQ05iAa5iAedKnhYamDoCNGo1ibq+=e4ksnx20GK1ssPDDpxaAbKKiDD==; ssxmod_itna2=YqRx2C0QoCqrDXKDHD0Q5iqdx0xiq2HPG=aeQK8KoD6ctlZ2D0vrrP03Dcl2Mn2FtqqTWhKGFKmkE2m1KSkvhme+RMYR1qcpGWRpiTQGIt2ebbeS5fSYtATFbgiIYyBniLsVdROn6uLm9OEUb7isS+QV9SIMA4oqnoIM/GIxF4uM9hI1GRDsbGTb3jRtvTEMtbKSeMi=rbQtpmt5OwKZ7hNh+cWpjqoLe=o5Awh=TkD1+CUejQRNDzGw13bXAqUMtQ9w6Fa08WkkFuWblxWTOORiv64snCx87BuIESw0ev9pYgiA8IuLOGIPmNDPp15RW0hYKRe0Uipq9mqEq1jw/Q+8Z0xrepe3Y1wpP4mPE3eRUmPKjjxjpeGItbvgi+X7G6B5e9o3/At6N1RGucmOPuMBbnrLf6wwoLx6pU0oKpwI/m82wXDQsW0dh6kfRkSq6CubrYYRmP8o1Cc8C9CGcpCanYWv1olcG2rFlBYPrwgA2peEcbKyePdgY2lpjOWqMN0/U1rd1iGP==SBr0A5fpP4h6AfmCcmPc6IWwWgy=DEUPYrvLrFfeDoLjvFIeMCF+tcxi4t6Q+72jSy2em/99wnH+7GkWKk5wFDG2mnQte6i22Y2vC55jxrmztAztbxDFqD+axxD===; Hm_lpvt_9793f42b498361373512340937deb2a0=1738494183"
resp=requests.get(url,headers={
    "Cookie":cookie
})
print(resp.text)
resp.close()
```



## 2.处理防盗链

防盗链：referer，溯源

在抓包工具中获取到对应视频流信息。会对视频流进行加工

受到了防盗链机制的保护。播放链接通常会经过服务器验证，确保只有通过正规途径的请求才能访问视频资源。

①.从原`url`中获取到视频编号`countID` ②.从`videostatus`中将获得的`src-url`中部分，替换为编号

```python
import requests
from lxml import etree
import re


paUrl="https://www.pearvideo.com/"
resp=requests.get(paUrl)

root=etree.HTML(resp.text)

sonPartUrl=root.xpath("/html/body/div[2]/div/div[2]/div//div/a/@href")
resp.close()

for sUrl in sonPartUrl:
    if re.match("video.*",sUrl):
        sonUrl=paUrl+sUrl#获取到子地址
        
        #获取视频编号
        conId=sonUrl.split("_")[1]
        
        videostatueUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={conId}"

        #加入防盗链
        header={
            "referer":sonUrl
        }
        resp=requests.get(videostatueUrl,headers=header)
        #获取视频信息用字典表示
        dic=resp.json()
        srcUrl=dic["videoInfo"]["videos"]["srcUrl"]
        systemTime=dic["systemTime"]

        trursrcUrl=srcUrl.replace(systemTime,f"cont-{conId}")
        print(trursrcUrl)

        #以二进制进行写入
        time=1
        try:
            print(f"正在下载视频{conId},这是第{time}次尝试...")
            with open(f"./梨视频/视频{conId}.mp4",mode='wb') as f:
                f.write(requests.get(trursrcUrl).content)
            print("下载完成")
        except:
            if time==3:
                print("下载失败")
            time+=1
            print("重新进行尝试")
        resp.close()

        
```



## 3.代理

使用代理服务器在客户端和目标服务器之间起到"代理"的作用，能够处理网络请求和响应的各种任务

```python
import requests

proxies={
   "https":"180.103.181.10"
}

resp=requests.get("https://www.baidu.com",proxies=proxies)
resp.encoding='utf-8'
print(resp)

```

## 实例：爬取网易云评论

①.从网络中捕获并提取包含评论信息的数据包。

②.从堆栈中定位并获取未加密前的原始参数

![image-20250211152437126](C:\Users\17677\AppData\Roaming\Typora\typora-user-images\image-20250211152437126.png)

③.处理加密过程

![image-20250211152858788](C:\Users\17677\AppData\Roaming\Typora\typora-user-images\image-20250211152858788.png)

a函数：产生16位随机字符串列，b函数为加密函数：`a`为加密文本，`b`为加密秘钥，对实参中g,i为定值秘钥

通过固定i值来获取到对应`params`和`encSecKey`

```python
import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="


data={
    "rid": "R_SO_4_2668124242",
    "threadId": "R_SO_4_2668124242",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}
#模拟加密过程

e='010001'
f='0085ddee518103f1aef177d3031a0b2fbf1595fb7d5c70afabcc3f356e0bdede8b2e40adc751df9ece1a62750ad1d9cdff976ead0a6f992b16a22abf1339e2b644fddfde23271723e113712c03a07c770be3a251d5a49fd1a9745acb8cabafefcd1c65d4d1409f5f0243a4587a6ded88802afc0a57f23f641a26cbacb4fdd6bf3f'
g='0CoJUm6Qyw8W8jud'

#取i为定值可以获得固定的encSacKey
i='SODmjau7C0M4YoM9'
iv="0102030405060708"#偏移量
def get_encSacKey():
    return '589a067630547fe842ef7729a1186321ffb0a2c7555eb0d5d74cdb35c5ffd550ecf766ae9cb2cafd37418e75988531d61b4fbe64843327b19576dec81e2c8a5af442792c6b4860cd5041ea3147c9faa39e41ab57a33feeedde3923e470d5b36add8b55d976ff1d3789a32c7f996b351e101d105ce040826419a0d4a1fd9cb116'

#加密函数，对应d函数
def get_params(data):#data对应着数据的字符串
    f=enc_params(data,g)
    s=enc_params(f,i)
    return s
#每一次的加密
def enc_params(data,key):
    obj=AES.new(key=key.encode("utf-8"),mode=AES.MODE_CBC ,iv=iv.encode("utf-8"))#创建加密器
    
    data=to_16(data)
    
    bs=obj.encrypt(data.encode("utf-8"))#获取加密字节,加密的长度必须为16倍数
    #将加密字节转换为能被utf-8识别并转换成字符串
    return str(b64encode(bs),"utf-8")


#转换字符串,拉长至16位
def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data
"""
def new(key, mode, *args, **kwargs):
    Create a new AES cipher.
    Args:
      key(bytes/bytearray/memoryview):
        The secret key to use in the symmetric cipher.
        It must be 16 (*AES-128)*, 24 (*AES-192*) or 32 (*AES-256*) bytes long.
                For ``MODE_SIV`` only, it doubles to 32, 48, or 64 bytes.
      mode (a ``MODE_*`` constant):
        The chaining mode to use for encryption or decryption.
        If in doubt, use ``MODE_EAX``.

    Keyword Args:
      iv (bytes/bytearray/memoryview):偏移量
        (Only applicable for ``MODE_CBC``, ``MODE_CFB``, ``MODE_OFB``,
        and ``MODE_OPENPGP`` modes).

        The initialization vector to use for encryption or decryption.

        For ``MODE_CBC``, ``MODE_CFB``, and ``MODE_OFB`` it must be 16 bytes long
"""

'''
params
encSacKey
'''


'''
function(json.stringrify(data),010001,'0085ddee518103f1aef177d3031a0b2fbf1595fb7d5c70afab
cc3f356e0bdede8b2e40adc751df9ece1a62750ad1d9cdff976ead0a6f992b16a22abf1339e2b644fddfde232
71723e113712c03a07c770be3a251d5a49fd1a9745acb8cabafefcd1c65d4d1409f5f0243a4587a6ded88802a
fc0a57f23f641a26cbacb4fdd6bf3f' ,0CoJUm6Qyw8W8jud )
'''

resp=requests.post(url,data={
    "params":get_params(json.dumps(data)),#需要将data从字典转换成json字符串,Python 对象（如字典、列表、字符串等）序列化为 JSON 格式的字符串
    "encSecKey":get_encSacKey()
})
print(resp.text)
```

# 四.爬取提速

多进程，多线程，协程

进程是资源单位，线程是执行单位

## 线程

```python
from threading import Thread

#start安排新线程来执行run

#使用target参数
def func():
    for i in range(20):
        print("func",i)

if __name__=="__main__":
    t=Thread(target=func)
    t.start()
    for i in range(20):
        print("main",i)

#重写run方法
class myThread(Thread):
    def run(self):
        for i in range(20):
            print("func",i)

if __name__=="__main__":
    t=myThread()
    t.start()
    for i in range(20):
        print("main",i)
```

## 进程

```python
from multiprocessing import Process
import time
#创建进程和线程的api高度相似
def func(a1):
    for i in range(100):
        print(f"子进程{a1}",i)

if __name__=="__main__":
    p=Process(target=func,args=("poppy",))#传参
    p.start()
    #time.sleep(1)由于进程启动的开销，子进程在加载过程中主进程先进行
    for i in range(100):
        print("主进程",i)
```

## 线程池和进程池

一次性开辟线程和进程，用户直接给线程/进程池提交任务，调度全部交给线程池调度。

### 简单的程序

```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(100):
        print(name,i)

if __name__=='__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):#将100个任务交给线程池
            t.submit(fn,name=f"任务{i}")
    #等待线程池任务全部执行完毕
    print("over")
```

