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
        



