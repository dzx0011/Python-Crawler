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