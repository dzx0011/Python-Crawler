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
