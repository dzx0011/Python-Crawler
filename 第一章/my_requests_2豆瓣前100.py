import requests
url="https://movie.douban.com/j/chart/top_list"

parame={
"type":"11",
"interval_id": "100:90",
"action": None,
"start": "0",
"limit": "100",
}
header={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

resp=requests.get(url,params=parame,headers=header)
answer_dir=resp.json()
for i in range(100):
    print(answer_dir[i]['rank'],answer_dir[i]['title'],answer_dir[i]['rating'])

resp.close()