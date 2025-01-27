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