import requests

proxies={
   "https":"180.103.181.10"
}

resp=requests.get("https://www.baidu.com",proxies=proxies)
resp.encoding='utf-8'
print(resp)

#180.103.181.10