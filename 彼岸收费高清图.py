#coding=gbk
import requests
from lxml import etree
#http://pic.netbian.com/e/extend/downpic.php?id=25487&t=0.2633914977585936
#http://pic.netbian.com/e/extend/downpic.php?id=24729&t=0.560255391360098
count=0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'Cookie': '__cfduid=d740c816be2b1ef5540da6cba01d2cea31582535194; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1582535197,1582536313; PHPSESSID=kommiass00nei57onuah0bm8b2; zkhanmlusername=qq_Weirdo717; zkhanmluserid=2722500; zkhanmlgroupid=1; zkhanmlrnd=Dw8belu3O10qNVRCjASZ; zkhanmlauth=5f25ff139f1825325470a4623e067b8f; zkhanpayphome=BuyGroupPay; zkhanpaymoneybgid=2; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1582541105',
    'Host': 'pic.netbian.com',
    'Referer': 'http://pic.netbian.com/tupian/24695.html'
}
url = 'http://pic.netbian.com/'
response = requests.get(url).content.decode('gbk')
html = etree.HTML(response)
#print(html)
href=html.xpath('//*[@id="main"]/div[3]/ul/li/a/@href')
#print(href)
for i in href:
    #print(i)
    ID=i[8:13]
    urls='http://pic.netbian.com/downpic.php?id='+ ID + '&classid=66'
    response1=requests.get(urls,headers=headers)
    f=open('彼岸图/{}.jpg'.format(count),'ab')
    count += 1
    f.write(response1.content)
    f.close()



