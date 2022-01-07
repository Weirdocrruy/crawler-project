# coding=gbk
import requests
from lxml import etree
import re
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
fp = open(r'C:\Users\Lenovo-PC\Desktop\天天基金股票型.csv', 'wt', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('name', 'type', 'Netvalue', 'growth', 'allgrowth', 'contents_list'))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Host': 'fund.eastmoney.com',
    'Cookie': 'EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND0=null; EMFUND6=12-31%2020%3A26%3A23@%23%24%u519C%u94F6%u65B0%u80FD%u6E90%u4E3B%u9898@%23%24002190; EMFUND7=12-31%2020%3A27%3A03@%23%24%u5DE5%u94F6%u6218%u7565%u65B0%u5174%u4EA7%u4E1A%u6DF7%u5408C@%23%24006616; EMFUND8=12-31%2020%3A27%3A08@%23%24%u524D%u6D77%u5F00%u6E90%u533B%u7597%u5065%u5EB7A@%23%24005453; st_si=91278095204737; st_asi=delete; FundWebTradeUserInfo=JTdCJTIyQ3VzdG9tZXJObyUyMjolMjIlMjIsJTIyQ3VzdG9tZXJOYW1lJTIyOiUyMiUyMiwlMjJWaXBMZXZlbCUyMjolMjIlMjIsJTIyTFRva2VuJTIyOiUyMiUyMiwlMjJJc1Zpc2l0b3IlMjI6JTIyJTIyLCUyMlJpc2slMjI6JTIyJTIyJTdE; EMFUND9=12-31%2020%3A29%3A31@%23%24%u534E%u590F%u65B0%u5174%u6D88%u8D39%u6DF7%u5408A@%23%24005888; EMFUND5=01-02 14:37:43@#$%u519C%u94F6%u5DE5%u4E1A4.0%u6DF7%u5408@%23%24001606; ASP.NET_SessionId=g4i1luik3scfxrow5bfafnwi; st_pvi=00792473333786; st_sp=2020-12-31%2020%3A01%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=5; st_psi=20210102143819838-0-3299429591'}


# url = 'http://fund.eastmoney.com/daogou/#dt4;ftgp;rs;sd;ed;pr;cp;rt;tp;rk;se;nx;sc3y;stdesc;pi1;pn20;zfdiy;shlist'
def main(url1):
    res = requests.get(url1, headers=headers)
    res.encoding = 'utf-8'
    tree = etree.HTML(res.text)
    hrefs = tree.xpath('//*[@id="fund_list"]/tbody/tr/td[2]/a/@href')
    names = tree.xpath('//*[@id="fund_list"]/tbody/tr/td[2]/a/text()')
    types = tree.xpath('//*[@id="fund_list"]/tbody/tr/td[3]/text()')
    Netvalues = tree.xpath('//*[@id="fund_list"]/tbody/tr/td[4]/span[1]/text()')
    growths = tree.xpath('//*[@id="fund_list"]/tbody/tr/td[8]/span/text()')
    allgrowths = tree.xpath('//*[@id="fund_list"]/tbody/tr/td[10]/span/text()')
    headers1 = {
        'Referer': 'http://fund.eastmoney.com/fund_favor_quote2_beta.html?v=dddgg',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Cookie': 'EMFUND1=null; EMFUND2=null; EMFUND3=null; st_si=01385149102410; ASP.NET_SessionId=zfvfjac32wwhj5pfc0a4sqps; st_asi=delete; _adsame_fullscreen_16928=1; qgqp_b_id=2c837850bc7ba349ba4e549fe2cb9c84; FundWebTradeUserInfo=JTdCJTIyQ3VzdG9tZXJObyUyMjolMjIlMjIsJTIyQ3VzdG9tZXJOYW1lJTIyOiUyMiUyMiwlMjJWaXBMZXZlbCUyMjolMjIlMjIsJTIyTFRva2VuJTIyOiUyMiUyMiwlMjJJc1Zpc2l0b3IlMjI6JTIyJTIyLCUyMlJpc2slMjI6JTIyJTIyJTdE; EMFUND0=null; EMFUND4=01-03%2013%3A19%3A14@%23%24%u519C%u94F6%u5DE5%u4E1A4.0%u6DF7%u5408@%23%24001606; EMFUND5=12-31%2020%3A26%3A23@%23%24%u519C%u94F6%u65B0%u80FD%u6E90%u4E3B%u9898@%23%24002190; EMFUND6=12-31%2020%3A27%3A03@%23%24%u5DE5%u94F6%u6218%u7565%u65B0%u5174%u4EA7%u4E1A%u6DF7%u5408C@%23%24006616; EMFUND7=12-31%2020%3A27%3A08@%23%24%u524D%u6D77%u5F00%u6E90%u533B%u7597%u5065%u5EB7A@%23%24005453; EMFUND8=12-31%2020%3A29%3A31@%23%24%u534E%u590F%u65B0%u5174%u6D88%u8D39%u6DF7%u5408A@%23%24005888; EMFUND9=01-03 13:58:23@#$%u6C47%u4E30%u664B%u4FE1%u4F4E%u78B3%u5148%u950B%u80A1%u7968@%23%24540008; st_pvi=00792473333786; st_sp=2020-12-31%2020%3A01%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=11; st_psi=20210103135839475-0-7307942322'
    }
    contents_lists = []
    for href in hrefs:
        detail_urls = 'http://fundf10.eastmoney.com/jjjl_' + href.split('/')[-1]
        # print(detail_urls)
        response = requests.get(detail_urls, headers=headers1)
        # print(response.text)
        contents = re.findall(
            '<strong>(.*?)</strong><a .*?>(.*?)</a></p><p><strong>(.*?)</strong>(.*?)</p><p>(.*?)</p>',
            response.text, re.S)
        contents = ''.join(str(contents)).strip()
        contents_lists.append(contents)

    for name, type, Netvalue, growth, allgrowth, contents_list in zip(names, types, Netvalues, growths, allgrowths,
                                                                      contents_lists):
        data = {
            'name': name,
            'type': type,
            'Netvalue': Netvalue,
            'growth': growth,
            'allgrowth': allgrowth,
            'contents_list': contents_list
        }
        print(data)
        writer.writerow((name, type, Netvalue, growth, allgrowth, contents_list))


if __name__ == '__main__':
    # urls = [
    #     'http://fund.eastmoney.com/daogou/#dt4;ftgp;rs;sd;ed;pr;cp;rt;tp;rk;se;nx;sc3y;stdesc;pi2;pn20;zfdiy;shlist'.format(i)
    #     for i in range(1, 50)]
    # for url in urls:
    url = 'http://fund.eastmoney.com/daogou/#dt4;ftgp;rs;sd;ed;pr;cp;rt;tp;rk;se;nx;sc3y;stdesc;pi2;pn20;zfdiy;shlist'
    main(url)
'''
http://fund.eastmoney.com/daogou/#dt4;ftgp;rs;sd;ed;pr;cp;rt;tp;rk;se;nx;sc3y;stdesc;pi1;pn20;zfdiy;shlist
http://fund.eastmoney.com/daogou/#dt4;ftgp;rs;sd;ed;pr;cp;rt;tp;rk;se;nx;sc3y;stdesc;pi3;pn20;zfdiy;shlist
'''