import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="


data={
    "rid": "R_SO_4_2668124242",
    "threadId": "R_SO_4_2668124242",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}
#模拟加密过程

e='010001'
f='0085ddee518103f1aef177d3031a0b2fbf1595fb7d5c70afabcc3f356e0bdede8b2e40adc751df9ece1a62750ad1d9cdff976ead0a6f992b16a22abf1339e2b644fddfde23271723e113712c03a07c770be3a251d5a49fd1a9745acb8cabafefcd1c65d4d1409f5f0243a4587a6ded88802afc0a57f23f641a26cbacb4fdd6bf3f'
g='0CoJUm6Qyw8W8jud'

#取i为定值可以获得固定的encSacKey
i='SODmjau7C0M4YoM9'
iv="0102030405060708"#偏移量
def get_encSacKey():
    return '589a067630547fe842ef7729a1186321ffb0a2c7555eb0d5d74cdb35c5ffd550ecf766ae9cb2cafd37418e75988531d61b4fbe64843327b19576dec81e2c8a5af442792c6b4860cd5041ea3147c9faa39e41ab57a33feeedde3923e470d5b36add8b55d976ff1d3789a32c7f996b351e101d105ce040826419a0d4a1fd9cb116'

#加密函数，对应d函数
def get_params(data):#data对应着数据的字符串
    f=enc_params(data,g)
    s=enc_params(f,i)
    return s
#每一次的加密
def enc_params(data,key):
    obj=AES.new(key=key.encode("utf-8"),mode=AES.MODE_CBC ,iv=iv.encode("utf-8"))#创建加密器
    
    data=to_16(data)
    
    bs=obj.encrypt(data.encode("utf-8"))#获取加密字节,加密的长度必须为16倍数
    #将加密字节转换为能被utf-8识别并转换成字符串
    return str(b64encode(bs),"utf-8")


#转换字符串,拉长至16位
def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data
"""
def new(key, mode, *args, **kwargs):
    Create a new AES cipher.
    Args:
      key(bytes/bytearray/memoryview):
        The secret key to use in the symmetric cipher.
        It must be 16 (*AES-128)*, 24 (*AES-192*) or 32 (*AES-256*) bytes long.
                For ``MODE_SIV`` only, it doubles to 32, 48, or 64 bytes.
      mode (a ``MODE_*`` constant):
        The chaining mode to use for encryption or decryption.
        If in doubt, use ``MODE_EAX``.

    Keyword Args:
      iv (bytes/bytearray/memoryview):偏移量
        (Only applicable for ``MODE_CBC``, ``MODE_CFB``, ``MODE_OFB``,
        and ``MODE_OPENPGP`` modes).

        The initialization vector to use for encryption or decryption.

        For ``MODE_CBC``, ``MODE_CFB``, and ``MODE_OFB`` it must be 16 bytes long
"""

'''
params
encSacKey
'''


'''
function(json.stringrify(data),010001,'0085ddee518103f1aef177d3031a0b2fbf1595fb7d5c70afab
cc3f356e0bdede8b2e40adc751df9ece1a62750ad1d9cdff976ead0a6f992b16a22abf1339e2b644fddfde232
71723e113712c03a07c770be3a251d5a49fd1a9745acb8cabafefcd1c65d4d1409f5f0243a4587a6ded88802a
fc0a57f23f641a26cbacb4fdd6bf3f' ,0CoJUm6Qyw8W8jud )
'''

resp=requests.post(url,data={
    "params":get_params(json.dumps(data)),#需要将data从字典转换成json字符串,Python 对象（如字典、列表、字符串等）序列化为 JSON 格式的字符串
    "encSecKey":get_encSacKey()
})
print(resp.text)