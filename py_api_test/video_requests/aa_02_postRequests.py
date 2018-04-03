import requests
import json

# url = "http://www.httpbin.org/post"
# file = {"file": open("readme.txt", "rb")}
# r = requests.post(url, files=file)
# print(r.text)


url = "http://httpbin.org/post"

image_files = [("image",("qqq.jpg",open("qqq.jpg","rb"),"image/jpg"))]

r= requests.post(url,files = image_files)
print(r.text)