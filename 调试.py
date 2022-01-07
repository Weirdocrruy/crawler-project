#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=gbk
from bs4 import BeautifulSoup
from lxml import etree
import requests
import csv
import time
import re
import pymongo
import json
import random
import pprint
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


'''headers = {
    'Referer': 'https://maoyan.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
response = requests.get('https://maoyan.com/films?showType=2&offset=0', headers=headers)
html = response.text
#print(html)
html1 = etree.HTML(html)
#print(html1)
num=html1.xpath
#mp4_url = html1.xpath('//*[@id="JprismPlayer"]/B站video/@src')
# mp4_url =re.findall('srcUrl="(.*?)"',html)
# print(mp4_url)'''
# url='https://maoyan.com/films/1217023'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
#     'Referer': 'https://maoyan.com/films?showType=2&offset=90',
#     'Host': 'maoyan.com',
#     'Cookie': '__mta=143465994.1582791146204.1582806618576.1582806696490.14; uuid_n_v=v1; uuid=E29F6900593811EA9F0985C24ED856C3F46C9F3C23E9418C925C077CADB727AB; _csrf=c854300670ee9cde961420eb63e44f162f28a893180856d11c30b11e4820e865; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=17085b436a49-087229b8913f55-4313f6b-100200-17085b436a5c8; _lxsdk=E29F6900593811EA9F0985C24ED856C3F46C9F3C23E9418C925C077CADB727AB; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1582791145; mojo-uuid=0219640175daf0d972262b01c65d4aac; mojo-session-id={"id":"fc9469ac0d2fa21e3001e28be0e751a9","time":1582806618391}; mojo-trace-id=5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1582806789; __mta=143465994.1582791146204.1582806696490.1582806789011.15; _lxsdk_s=17086975a30-fd1-77e-8bd%7C%7C11',
#
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1'
# }
# response=requests.get(url,headers=headers)
# print(response.text)
# html = etree.HTML(response.text)
# actors =html.xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/div/div[2]/ul/li/div/a/text()')
# #print(actors)
# actors1 = ''.join(actors)
# a=[]
# b=a.append(actors1)
# print(a)
#actor2 = map(str,actors1)
# print(actor2)
#l = eval(actor2)
# actors2= str.split ('\n')
# print(actors1)
#print(l)
# actors2 = eval(str(actors1))
# actors=re.findall('<img class="default-img" alt=" (.*?)" />',response.text)

# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
#     'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=3'
# }
# data={
#     'first': 'true',
#     'pn': 1,
#     'kd': 'python'
# }
#
# session = requests.session()
# session.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=3', headers=headers)
# cookies = session.cookies
# cookies.get_dict()
# print(cookies.get_dict())
#
# rep=requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',data=data,headers=headers,cookies=cookies)
# print(rep.text)
# pprint.pprint(rep.text)
#
# qq_lists = []
# fp = open(r'C:\Users\Lenovo-PC\Desktop\QQmail.csv')
# reader = csv.DictReader(fp)
# for row in reader:
#     qq_lists.append(row['电子邮件'].split('@')[0])
# fp.close()
# for item in qq_lists:
#     print(item)

# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
#     'Host': 'fund.eastmoney.com',
#     'Cookie':'EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND0=null; EMFUND6=12-31%2020%3A26%3A23@%23%24%u519C%u94F6%u65B0%u80FD%u6E90%u4E3B%u9898@%23%24002190; EMFUND7=12-31%2020%3A27%3A03@%23%24%u5DE5%u94F6%u6218%u7565%u65B0%u5174%u4EA7%u4E1A%u6DF7%u5408C@%23%24006616; EMFUND8=12-31%2020%3A27%3A08@%23%24%u524D%u6D77%u5F00%u6E90%u533B%u7597%u5065%u5EB7A@%23%24005453; st_si=91278095204737; st_asi=delete; FundWebTradeUserInfo=JTdCJTIyQ3VzdG9tZXJObyUyMjolMjIlMjIsJTIyQ3VzdG9tZXJOYW1lJTIyOiUyMiUyMiwlMjJWaXBMZXZlbCUyMjolMjIlMjIsJTIyTFRva2VuJTIyOiUyMiUyMiwlMjJJc1Zpc2l0b3IlMjI6JTIyJTIyLCUyMlJpc2slMjI6JTIyJTIyJTdE; EMFUND9=12-31%2020%3A29%3A31@%23%24%u534E%u590F%u65B0%u5174%u6D88%u8D39%u6DF7%u5408A@%23%24005888; EMFUND5=01-02 14:37:43@#$%u519C%u94F6%u5DE5%u4E1A4.0%u6DF7%u5408@%23%24001606; ASP.NET_SessionId=g4i1luik3scfxrow5bfafnwi; st_pvi=00792473333786; st_sp=2020-12-31%2020%3A01%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=5; st_psi=20210102143819838-0-3299429591'}
# urls='http://fund.eastmoney.com/trade/hh.html?spm=001.1.swh#zwf_,sc_1n,st_desc'
# response = requests.get(urls,headers=headers)
# response.encoding = 'gbk'
# print(response.text)
import requests
from lxml import etree

# import requests
# from lxml import etree
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
#     'Referer': 'https://maoyan.com/films?showType=2&offset=90',
#     'Host': 'maoyan.com',
#     'Cookie': '__mta=143465994.1582791146204.1582806618576.1582806696490.14; uuid_n_v=v1; uuid=E29F6900593811EA9F0985C24ED856C3F46C9F3C23E9418C925C077CADB727AB; _csrf=c854300670ee9cde961420eb63e44f162f28a893180856d11c30b11e4820e865; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=17085b436a49-087229b8913f55-4313f6b-100200-17085b436a5c8; _lxsdk=E29F6900593811EA9F0985C24ED856C3F46C9F3C23E9418C925C077CADB727AB; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1582791145; mojo-uuid=0219640175daf0d972262b01c65d4aac; mojo-session-id={"id":"fc9469ac0d2fa21e3001e28be0e751a9","time":1582806618391}; mojo-trace-id=9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1582807813; __mta=143465994.1582791146204.1582806696490.1582807812838.15; _lxsdk_s=17086975a30-fd1-77e-8bd%7C%7C19',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1'
# }
#
# url = 'https://www.maoyan.com/board/4?offset=0'
# res = requests.get(url, headers=headers)
# res.encoding = 'utf-8'
# print(res.text)

