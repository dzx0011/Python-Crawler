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





