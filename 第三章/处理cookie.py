import requests


#session会话，cookie不丢失
session=requests.session()
header={
    "origin":"https://passport.17k.com",
    "referer":"https://passport.17k.com/login/",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

data={
    "loginName": "18250927959",
    "password": "chenhezhuma1"
}

url="https://passport.17k.com/ck/user/login"
resp=session.post(url,data=data,headers=header)
print(resp.cookies)



#2.直接获取到cookie给程序
url="https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"
cookie="GUID=344bac05-ed7a-4a04-9648-8f897ff38af9; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F12%252F12%252F30%252F103983012.jpg-88x88%253Fv%253D1738486407000%26id%3D103983012%26nickname%3Dbilibili111%26e%3D1754040296%26s%3D5d9fd296288f79ab; tfstk=gj7oZlgIGg-7fm6tet87fVct-yqvNbTBc93ppepU0KJXp79Je6Wht1-ea4WRmpXVnL8pyaUhxK8yAgppepYhOOVYBPUON_TBbReTWFSYUsY6abJrpnk2TeAPmynay_TB8-E1OxMPNOrjatFH8SY2tBuy82We0IJXOBkyT4PcgK9qzBRr8j52_Coy8eWFgSAB3QkseD9GFOQ4nmoA3EjfdZAkqd50fq0qfQk9L_Jo82JkZ3mcaK0E8ZjYWhdBUlGvdUp5NQXQ54TyxM7Juay48FS1nwxwSkFW7a1FfM5jEWvPMT_MzN2oyIKHEi7ymXueuEIybMXuE09P2tx6gnl35IB93__PmWMVaOpkzI-Y75f2YiQWfaeqrFS1wUIFQ-nJUGAF47nqbIfjRIPdoDiB4IODBq1JkCdXpKDYiSm_u3RXNrV0iDiB4IODBSVmfr-yGQac.; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103983012%22%2C%22%24device_id%22%3A%22194c5dc67b5fc6-0f7f26b4b5a356-26011b51-1821369-194c5dc67b61e32%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22344bac05-ed7a-4a04-9648-8f897ff38af9%22%7D; acw_sc__v2=679f506d879617ea2c360070b7bd0701de6f36cc; Hm_lvt_9793f42b498361373512340937deb2a0=1738486344,1738494067; HMACCOUNT=BE7DBABC5B2E8C13; ssxmod_itna=YqRx2C0QoCqrDXKDHD0Q5iqdx0xiq2HPG=aeQK8Ko8DlODWqeGzDAxn40iDtxhVETPoaKeLbj7Ut98TPK03xcoWr3LB87KDHxY=DUpYuGhD4+5GwD0eG+DD4DWDmnHDnxAQDjxGPyn2v5CDYPDEB5DRcPDu=AhDGc1Uh9hDeKD0OTHDQI+2axDBahAaWKqpahhDiWH5zvIcpifK7GkD7v+DlaQBFhkFIMUanHf2tdhUGKDXpQDvpHmnEge2Zvze325UQ05iAa5iAedKnhYamDoCNGo1ibq+=e4ksnx20GK1ssPDDpxaAbKKiDD==; ssxmod_itna2=YqRx2C0QoCqrDXKDHD0Q5iqdx0xiq2HPG=aeQK8KoD6ctlZ2D0vrrP03Dcl2Mn2FtqqTWhKGFKmkE2m1KSkvhme+RMYR1qcpGWRpiTQGIt2ebbeS5fSYtATFbgiIYyBniLsVdROn6uLm9OEUb7isS+QV9SIMA4oqnoIM/GIxF4uM9hI1GRDsbGTb3jRtvTEMtbKSeMi=rbQtpmt5OwKZ7hNh+cWpjqoLe=o5Awh=TkD1+CUejQRNDzGw13bXAqUMtQ9w6Fa08WkkFuWblxWTOORiv64snCx87BuIESw0ev9pYgiA8IuLOGIPmNDPp15RW0hYKRe0Uipq9mqEq1jw/Q+8Z0xrepe3Y1wpP4mPE3eRUmPKjjxjpeGItbvgi+X7G6B5e9o3/At6N1RGucmOPuMBbnrLf6wwoLx6pU0oKpwI/m82wXDQsW0dh6kfRkSq6CubrYYRmP8o1Cc8C9CGcpCanYWv1olcG2rFlBYPrwgA2peEcbKyePdgY2lpjOWqMN0/U1rd1iGP==SBr0A5fpP4h6AfmCcmPc6IWwWgy=DEUPYrvLrFfeDoLjvFIeMCF+tcxi4t6Q+72jSy2em/99wnH+7GkWKk5wFDG2mnQte6i22Y2vC55jxrmztAztbxDFqD+axxD===; Hm_lpvt_9793f42b498361373512340937deb2a0=1738494183"
resp=requests.get(url,headers={
    "Cookie":cookie
})
print(resp.text)
resp.close()
