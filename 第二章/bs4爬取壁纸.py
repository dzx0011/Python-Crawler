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

    



