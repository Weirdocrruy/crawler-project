# coding = gbk
# coding:utf-8

import requests
import re
import execjs
import js2py
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

domain = 'https://www.dytt8.net/index.htm'
resp = requests.get(domain)  # verify=False
resp.encoding = 'gbk'
#print(resp.text)

obj1 = re.compile(r"2021新片精品.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"最新电影下载.*?<a href='(?P<href>.*?)'", re.S)
result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')
    # print(ul)
    result2 = obj2.finditer(ul)
    for itt in result2:
        child_href = domain + itt.group('href')
        child_resp = requests.get(child_href, headers=headers)
        print(child_resp.text)
        js = "<script language=javascript>window.location.href='https://www.dytt8.net/html/gndy/dyzz/index.html</script>"
        # execjs.eval(js)
        # js2py.eval_js(js)
        print(child_resp.text)
        break
#         child_href_list.append(child_href)
#
# for href in child_href_list:
#     child_resp = requests.get(href)
#     child_resp.encoding = 'gbk'
#     print(child_resp.text)
#     break   # 测试