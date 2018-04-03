import requests
import  json


url = "http://www.httpbin.org/get"
parmas = {"show_env":1}

r = requests.get(url,parmas)
# r.status_code
print(r.status_code, r.reason)  #状态码 结果
print(r.headers)
print(r.text)
# print(r.content) #二进制文本
print(r.request.headers)

# re = r.json()
# print(re)


