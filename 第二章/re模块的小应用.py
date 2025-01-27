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
    #re.S让.可以代替\n
    para={
    "start":str(start),
    "filter":""
    }

  
    resp=requests.get(url,headers=header,params=para)
    
    time.sleep(1)  # 每次请求之间等待1秒防止被短期封锁

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