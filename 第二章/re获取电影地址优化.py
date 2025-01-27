import requests
import re
import time

url = "https://www.dytt89.com/"

head = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# 正则表达式对象
obj1 = re.compile(r'<span style="float:left;">2024必看热片</span>.*?<ul>(?P<movieDetail>.*?)</ul>', flags=re.S)
obj2 = re.compile(r"<li><a href=[\"'](?P<href>.*?)[\"'] title=[\"'](?P<title>.*?)[\"']>.*?</li>", flags=re.S)
obj3 = re.compile(r'<div id="downlist".*?<a href="(?P<aurl>.*?)".*?</div>', flags=re.S)

try:
    # 获取主页面
    resp = requests.get(url, headers=head, timeout=5)
    resp.encoding = "gb2312"
    result1 = obj1.finditer(resp.text)
    resp.close()
    
    # 遍历每个电影的详情链接
    for i in result1:
        result2 = obj2.finditer(i.group('movieDetail'))
        
        sub_head = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Referer": url
        }

        for j in result2:
            url_t = url + j.group('href').strip('/')
            print(f"正在处理链接：{url_t}")

            # 尝试访问子页面，重试机制
            retries = 3  # 重试次数
            while retries > 0:
                try:
                    resp_sub = requests.get(url_t, headers=sub_head, timeout=5)
                    resp_sub.encoding = "gb2312"
                    result3 = obj3.search(resp_sub.text)
                    resp_sub.close()

                    if result3:
                        download_url = result3.group('aurl')
                        print(f"获取到下载链接：{download_url}")

                        # 逐行写入文件
                        with open("downloadURL.txt", mode='a', encoding='gbk') as f:
                            f.write(download_url + '\n')
                    else:
                        print(f"未找到下载链接：{url_t}")
                    
                    break  # 成功时退出重试
                except Exception as e:
                    retries -= 1
                    print(f"访问失败，重试中... 剩余尝试次数：{retries}")
                    time.sleep(2)  # 等待2秒后重试
            
            if retries == 0:
                print(f"最终失败，跳过链接：{url_t}")

except Exception as e:
    print(f"程序运行时发生错误: {e}")
