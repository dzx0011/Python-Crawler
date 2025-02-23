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

        


