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
        
        

        
        

