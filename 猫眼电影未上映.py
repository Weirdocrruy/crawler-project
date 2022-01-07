# coding=gbk
# -*- coding: UTF-8 -*-
import requests
import re
import io
import sys
import csv
import time
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

fp = open(r'C:\Users\Lenovo-PC\Desktop\猫眼电影.csv', 'wt', newline='',encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('title', 'content','actor'))


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Referer': 'https://maoyan.com/films?showType=2&offset=90',
    'Host': 'maoyan.com',
    'Cookie': '__mta=143465994.1582791146204.1582806618576.1582806696490.14; uuid_n_v=v1; uuid=E29F6900593811EA9F0985C24ED856C3F46C9F3C23E9418C925C077CADB727AB; _csrf=c854300670ee9cde961420eb63e44f162f28a893180856d11c30b11e4820e865; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=17085b436a49-087229b8913f55-4313f6b-100200-17085b436a5c8; _lxsdk=E29F6900593811EA9F0985C24ED856C3F46C9F3C23E9418C925C077CADB727AB; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1582791145; mojo-uuid=0219640175daf0d972262b01c65d4aac; mojo-session-id={"id":"fc9469ac0d2fa21e3001e28be0e751a9","time":1582806618391}; mojo-trace-id=9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1582807813; __mta=143465994.1582791146204.1582806696490.1582807812838.15; _lxsdk_s=17086975a30-fd1-77e-8bd%7C%7C19',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}
def get_info(url):
    response = requests.get(url, headers=headers)
    html = response.text
    #print(html)
    hrefs = re.findall('href="(.*?)" target="_blank" data-act="movies-click"', html)
    #print(hrefs)
    for href in hrefs:
        #print(href)
        url = 'https://maoyan.com' + href
        #print(url)

        response = requests.get(url, headers=headers)
        #print(response.text)
        html = etree.HTML(response.text)
        actors = html.xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/div/div[2]/ul/li/div/a/text()')
        # print(actors)
        actors1 = ''.join(actors)
        a = []
        b = a.append(actors1)
        print(a)

        response = requests.get(url, headers=headers).text
        # print(response)
        titles = re.findall('<h1 class="name">(.*?)</h1>', response)
        #print(titles)
        contents = re.findall('<span class="dra">(.*?)</span>', response)
        #html = etree.HTML(response)
        #actors = html.xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/div/div[2]/ul/li/div/a/text()')
        #print(actors)
        #actors1 = ''.join(actors)
        #actors2 =str.split(actors1)
        #print(contents)
        for title, content,actor in zip(titles, contents,a):
            info = {
                'title': title,
                'content': content,
                'actor':actor
            }
            #print(info)
            title=info['title']
            content=info['content']
            actor=info['actor']

            writer.writerow((title,content,actor))

fp.close()

if __name__ == '__main__':
    urls = ['https://maoyan.com/films?showType=2&offset={}'.format(i) for i in range(0, 90,30)]
    for url in urls:
        get_info(url)
        time.sleep(1)




