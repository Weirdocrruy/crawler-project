# coding=gbk
import requests
from lxml import etree
import re
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
fp = open(r'C:\Users\Lenovo-PC\Desktop\天天基金.csv', 'wt', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('name', 'Netvalue', 'growth', 'allgrowth', 'contents_list'))

headers = {
    'Cookie': 'EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND0=null; EMFUND6=12-31%2020%3A26%3A23@%23%24%u519C%u94F6%u65B0%u80FD%u6E90%u4E3B%u9898@%23%24002190; EMFUND7=12-31%2020%3A27%3A03@%23%24%u5DE5%u94F6%u6218%u7565%u65B0%u5174%u4EA7%u4E1A%u6DF7%u5408C@%23%24006616; EMFUND8=12-31%2020%3A27%3A08@%23%24%u524D%u6D77%u5F00%u6E90%u533B%u7597%u5065%u5EB7A@%23%24005453; EMFUND9=12-31%2020%3A29%3A31@%23%24%u534E%u590F%u65B0%u5174%u6D88%u8D39%u6DF7%u5408A@%23%24005888; EMFUND5=01-03 13:19:14@#$%u519C%u94F6%u5DE5%u4E1A4.0%u6DF7%u5408@%23%24001606; st_si=01385149102410; ASP.NET_SessionId=zfvfjac32wwhj5pfc0a4sqps; st_asi=delete; _adsame_fullscreen_16928=1; qgqp_b_id=2c837850bc7ba349ba4e549fe2cb9c84; FundWebTradeUserInfo=JTdCJTIyQ3VzdG9tZXJObyUyMjolMjIlMjIsJTIyQ3VzdG9tZXJOYW1lJTIyOiUyMiUyMiwlMjJWaXBMZXZlbCUyMjolMjIlMjIsJTIyTFRva2VuJTIyOiUyMiUyMiwlMjJJc1Zpc2l0b3IlMjI6JTIyJTIyLCUyMlJpc2slMjI6JTIyJTIyJTdE; st_pvi=00792473333786; st_sp=2020-12-31%2020%3A01%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=6; st_psi=20210103132029189-0-0872616394',
    'Host': 'fund.eastmoney.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
url = 'http://fund.eastmoney.com/trade/gp.html'
res = requests.get(url, headers=headers)
res.encoding = 'gbk'
tree = etree.HTML(res.text)
hrefs = tree.xpath('//*[@id="tblite_gp"]/tbody/tr/td[2]/a/@href')
# print(hrefs)
names = tree.xpath('//*[@id="tblite_gp"]/tbody/tr/td[2]/a/text()')
Netvalues = tree.xpath('//*[@id="tblite_gp"]/tbody/tr/td[3]/span[1]/text()')
growths = tree.xpath('//*[@id="tblite_gp"]/tbody/tr/td[8]/text()')
allgrowths = tree.xpath('//*[@id="tblite_gp"]/tbody/tr/td[13]/text()')
headers1 = {
    'Referer': 'http://fund.eastmoney.com/fund_favor_quote2_beta.html?v=dddgg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': 'EMFUND1=null; EMFUND2=null; EMFUND3=null; st_si=01385149102410; ASP.NET_SessionId=zfvfjac32wwhj5pfc0a4sqps; st_asi=delete; _adsame_fullscreen_16928=1; qgqp_b_id=2c837850bc7ba349ba4e549fe2cb9c84; FundWebTradeUserInfo=JTdCJTIyQ3VzdG9tZXJObyUyMjolMjIlMjIsJTIyQ3VzdG9tZXJOYW1lJTIyOiUyMiUyMiwlMjJWaXBMZXZlbCUyMjolMjIlMjIsJTIyTFRva2VuJTIyOiUyMiUyMiwlMjJJc1Zpc2l0b3IlMjI6JTIyJTIyLCUyMlJpc2slMjI6JTIyJTIyJTdE; EMFUND0=null; EMFUND4=01-03%2013%3A19%3A14@%23%24%u519C%u94F6%u5DE5%u4E1A4.0%u6DF7%u5408@%23%24001606; EMFUND5=12-31%2020%3A26%3A23@%23%24%u519C%u94F6%u65B0%u80FD%u6E90%u4E3B%u9898@%23%24002190; EMFUND6=12-31%2020%3A27%3A03@%23%24%u5DE5%u94F6%u6218%u7565%u65B0%u5174%u4EA7%u4E1A%u6DF7%u5408C@%23%24006616; EMFUND7=12-31%2020%3A27%3A08@%23%24%u524D%u6D77%u5F00%u6E90%u533B%u7597%u5065%u5EB7A@%23%24005453; EMFUND8=12-31%2020%3A29%3A31@%23%24%u534E%u590F%u65B0%u5174%u6D88%u8D39%u6DF7%u5408A@%23%24005888; EMFUND9=01-03 13:58:23@#$%u6C47%u4E30%u664B%u4FE1%u4F4E%u78B3%u5148%u950B%u80A1%u7968@%23%24540008; st_pvi=00792473333786; st_sp=2020-12-31%2020%3A01%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=11; st_psi=20210103135839475-0-7307942322'
}
contents_lists = []
for href in hrefs:
    detail_urls = 'http://fundf10.eastmoney.com/jjjl_' + href.split('/')[-1]
    response = requests.get(detail_urls, headers=headers1)
    contents = re.findall('<strong>(.*?)</strong><a .*?>(.*?)</a></p><p><strong>(.*?)</strong>(.*?)</p><p>(.*?)</p>',
                          response.text, re.S)
    contents = ''.join(str(contents)).strip()
    # print(contents)
    contents_lists.append(contents)
print(contents_lists)
for name, Netvalue, growth, allgrowth, contents_list in zip(names, Netvalues, growths, allgrowths, contents_lists):
    data = {
        'name': name,
        'Netvalue': Netvalue,
        'growth': growth,
        'allgrowth': allgrowth,
        'contents_list': contents_list
    }
    writer.writerow((name, Netvalue, growth, allgrowth, contents_list))
'''
http://fund.eastmoney.com/trade/gp.html
http://fund.eastmoney.com/trade/gp.html
https://fundapi.eastmoney.com/fundtradenew.aspx?ft=gp&sc=1n&st=desc&pi=2&pn=100&cp=&ct=&cd=&ms=&fr=&plevel=&fst=&ftype=&fr1=&fl=0&isab=1
'''