#coding=gbk
import requests
import parsel
import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
for page in range(1,98):
    print('========������ȡ��{}ҳ����=====',format(page))
    #������ҳ
    base_url='https://www.umei.cc/meinvtupian/meinvxiezhen/{}.htm'.format(str(page))
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    #��������
    response=requests.get(base_url,headers=headers)
    #response.encoding=response.apparent_encoding  #ʶ�����
    html=response.text
    #print(html)
    #��������
    #3.1ת����������
    parse=parsel.Selector(html)
    #3.2������ȡ
    href_list=parse.xpath('//div[@class="TypeList"]/ul/li/a/@href').extract()
    #print(href_list)
    for href in href_list:
        #print(href)
        href_data=requests.get(href,headers=headers).text
        #print(href_data)

        #print(href_data)
        #����ͼƬ
        img=parsel.Selector(href_data)
        img_src=img.xpath('//div[@class="ImageBody"]/p/a/img/@src').extract_first()
        #print(img_src)

        #����ͼƬ��URL����
        if img_src:
            img_data = requests.get(img_src, headers=headers).content  # ������������ȡ

            # 4.���ݱ���
            # ׼��ͼƬ�ļ���
            file_name = img_src.split(['/'][0])
            file_name1 = file_name[-1]
            # file_name = re.findall('<meta name="keywords" content="(.*?)">',href_data)
            # print(file_name)
            # file_name1 = file_name[-1]
            # print(file_name1)

            #����
            with open('img\\' + file_name1, 'wb')as f:
                print('���ڱ��棺', file_name1)
                f.write(img_data)
