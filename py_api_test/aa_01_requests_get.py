#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json

url = "http://news.baidu.com/ns"
parmas = {"word": 123, "tn": "news",
          "from":"news","cl":2,"rn":20,"ct":1}
# r = requests.get(url,parmas)
r = requests.get(url, parmas)
print(r.status_code)
t = r.text
# print(t)
print(r.url)
# loads字符串转换字典
d = json.loads(str(t.encode("utf-8")))
print(d)
