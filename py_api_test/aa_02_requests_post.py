import requests

url = "https://www.douban.com/login"
data = {"email": "383195937@qq.com", "password": "77nicegay"}
r = requests.post(url, data)
print(r)
