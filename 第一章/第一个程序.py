from urllib.request import urlopen
url='https://www.baidu.com'
response = urlopen(url)
#windows默认为gbk
with open("mybaidu.html",mode='w',encoding='utf-8')as f:
    f.write(response.read().decode("utf-8"))
print("over")

#服务器渲染：在服务器将数据和html整合，统一返回浏览器
#客户端渲染：第一次请求只要一个html骨架，第二次请求拿到数据，进行数据展示，在源代码中看不到数据

#浏览器抓包工具

#HTTP协议
#请求：
#请求行：请求方式(post/get) 请求url 协议
#请求头：服务器附加信息
#请求体：请求参数
#响应
#状态行 协议 状态码 200,404,500,302
#响应头 放在客户端的附加信息
#响应体 真正返回客户端的内容HTML，json等

#请求头中重要内容
"""
import requests

url = 'https://www.baidu.com'
response = requests.get(url)

# 解码并写入文件
with open("mybaidu.html", mode='w', encoding='utf-8') as f:
    f.write(response.text)

print("over")
"""
