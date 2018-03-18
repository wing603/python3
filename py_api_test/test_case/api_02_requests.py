import requests

r = re.get("http://www.baidu.com")
# status 返回http请求状态 200成功404失败
s = r.status_code
print(s)
# text http响应内容字符串形式 头信息
t = r.text
print(t)
# 从http header中猜测响应内容编码方式
e = r.encoding
print(e)
# 从内容分析响应内容的编码方式
a = r.apparent_encoding
print(a)
# html响应的二进制编码方式
c = r.content()
print(c)
