# coding=gbk
import requests
from lxml import etree
import csv
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
fp = open(r'C:\Users\Lenovo-PC\Desktop\股票型.csv', 'wt', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('company', 'represent', 'Workingtime', 'Jobhoppingfrequency', 'Annualreturn', 'rank', 'details'))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
url = 'https://www.howbuy.com/fund/manager/ajax.htm'
for page in range(1, 20):
    data = {
        'wzfl': '',
        'cynx': '',
        'jgdm': '',
        'keyword': '',
        'ryzt': '',
        'orderField': 'rqzs',
        'orderType': 'true',
        'page': page
    }
    res = requests.post(url, headers=headers, data=data)
    response = json.loads(res.text)
    rydms = response['list']
    for rydm1 in rydms:
        rydm = 'https://www.howbuy.com/fund/manager/' + rydm1['rydm'] + '/'
        response1 = requests.get(rydm, headers=headers)
        html = etree.HTML(response1.text)
        company = html.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[2]/a/text()')
        company = ''.join(company).strip()
        represent = html.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[4]/a/text()')
        represent = ''.join(represent).strip()
        Workingtime = html.xpath('//div[@class="content_m fl"]/table//tr[1]/td[4]/text()')
        Workingtime = ''.join(Workingtime).strip()
        Jobhoppingfrequency = html.xpath('//div[@class="content_m fl"]/table//tr[2]/td[4]/text()')
        Jobhoppingfrequency = ''.join(Jobhoppingfrequency).strip()
        Annualreturn = html.xpath('//div[@class="content_m fl"]/table//tr[3]/td[4]/span/text()')
        Annualreturn = ''.join(Annualreturn).strip()
        rank = html.xpath('//*[@id="experience"]/div[3]/div[1]/div/div[3]/p[2]/text()')
        rank = [x.strip() for x in rank if x.strip() != '']
        rank = ''.join(rank).strip()
        details = html.xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/text()')
        details = [x.strip() for x in details if x.strip() != '']
        details = ''.join(details).strip()
        writer.writerow((company, represent, Workingtime, Jobhoppingfrequency, Annualreturn, rank, details))
        print(details)

'''
https://www.howbuy.com/fund/fundranking/gupiao.htm
http://fund.eastmoney.com/trade/hh.html?spm=001.1.swh#zwf_,sc_1n,st_desc
'''