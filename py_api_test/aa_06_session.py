# # -*- coding:utf-8 -*-
# # 获取cookie
# import requests
# import json
#
# url = "https://www.baidu.com/"
# r = requests.get(url)
# r.cookies
# # 将RequestsCookieJar转换成字典
# c = requests.utils.dict_from_cookiejar(r.cookies)
#
# print(c)
# print(r.cookies)
# for a in r.cookies:
#     print(a.name, a.value)

import requests
import json

host = "http://httpbin.org/"
endpoint = "cookies"

url = ''.join([host,endpoint])
url1 = "http://httpbin.org/cookies/set/sessioncookie/123456789"

r = requests.get(url)
print (r.text)

print ("------")


s = requests.session()    #初始化一个session对象
s.get(url1)               #cookie的信息存在了session中
r = s.get(url)

print (r.text)