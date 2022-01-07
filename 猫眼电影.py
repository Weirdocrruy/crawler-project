# coding = gbk
# -*- coding:utf-8 -*-

import requests
from lxml import etree
from fontTools.ttLib import TTFont
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Cookie': '__mta=146191883.1635950812324.1636036364787.1637419184428.24; uuid_n_v=v1; uuid=CC1DFD203CB411ECB5848BACA0C9469452F9B1DC7E614B96821466D352266819; _lxsdk_cuid=17ce643d298c8-047056bc65bcf-a7d193d-100200-17ce643d298c8; _lxsdk=CC1DFD203CB411ECB5848BACA0C9469452F9B1DC7E614B96821466D352266819; _csrf=1828c478e46ee4a9e141a5465a51930faff0dfd1fcefa8653849314875bc5028; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1636003674,1636016017,1636036357,1637418945; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=207861293.1635950777122.1636021717697.1637418950770.37; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1637419184; _lxsdk_s=17d3dc64b80-420-5cf-4cc%7C%7C14'
}

url = 'https://www.maoyan.com/films/1200486'
res = requests.get(url, headers=headers)
print(res.text)
font = re.findall("'\S+.woff'", res.text)[0]
font = eval(font)
print('https:'+font)
response = requests.get('https:'+font,headers = headers)
with open('woff_data','w',encoding='utf-8') as files:
    files.write(response.text)
template_font = TTFont(r'E:\Users\Lenovo-PC\PycharmProjects\python学习\小爬虫项目\woff_data')
template_font.saveXML('to.xml')