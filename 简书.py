#coding=gbk
import requests
import re
from multiprocessing import Pool
import  pymongo
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
jianshu = mydb['jianshu']

fp = open(r'C:\Users\Lenovo-PC\Desktop\简书.csv', 'wt', newline='', encoding='UTF-8-sig')
writer = csv.writer(fp)
writer.writerow(('name', 'content', 'score', 'author'))

#url='https://www.jianshu.com/c/bDHhpK'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': '_ga=GA1.2.1748486470.1583829168; __gads=ID=ddfc35353c5b4a2e:T=1583829168:S=ALNI_MZSAumAwmaenj6p8s4AkwrRVS2_gQ; _m7e_session_core=46a31ff2404ee6d40a873a8cb78cb46a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170c3932cdbad-02c063c720f4d8-3f6b4e04-1049088-170c3932cdc2bc%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%2C%22%24device_id%22%3A%22170c3932cdbad-02c063c720f4d8-3f6b4e04-1049088-170c3932cdc2bc%22%7D; __yadk_uid=SupCbbtlZB03KMYpxmJfV8hy7WzNgGQE; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fc%2FbDHhpK; read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1583829168,1583984411,1583984614,1583986424; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1583986424'
    }
def get_jianshu_info(url):
    html = requests.get(url,headers=headers).text
    #print(html)
    names =re.findall('<a class="title" target="_blank" href=.*?>(.*?)</a>',html)
    print(names)
    coments =re.findall('<p class="abstract">(.*?)</p>',html,re.S)
    print(coments)
    scores =re.findall(' <i class="iconfont ic-paid1"></i> (.*?)</span>',html,re.S)
    print(scores)
    authors =re.findall('<a class="nickname" target="_blank" href=.*?>(.*?)</a>',html)
    print(authors)
    for name,coment,score,author in zip(names,coments,scores,authors):
        data={
            'name':name,
            'coment':coment,
            'score':score,
            'author':author
        }
        print(data)
        jianshu.insert_one(data)
        writer.writerow((name, coment, score, author))

#get_jianshu_info(url)


if __name__ =='__main__':
    urls=['https://www.jianshu.com/c/bDHhpK?order_by=commented_at&page={}'.format(i) for i in range(1,300)]
    pool =Pool(processes=4)
    pool.map(get_jianshu_info,urls)
