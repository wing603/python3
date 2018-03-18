# import urllib.request
# import re
#
# def getHtml(url):
#     # urllib.urlopen()方法打开一个url地址
#     page = urllib.request.urlopen(url)
#     # read()方法读取url数据
#     html = page.read()
#     return html
#
#     def getImg(html):
#         reg = r'src="(.+?\.jpg)" pic_ext'
#         imgre = re.compile(reg)
#         imglist = re.findall(imgre,html)
#
# html = getHtml("http://www.sssabcd.com/index.html")
# print(html)

import re
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


html = getHtml("http://tieba.baidu.com/p/2460150866")
print (getImg(html))
