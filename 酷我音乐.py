#coding=gbk
import requests
import json
import os
# ����վ�з������ƣ�Ҫģ�������������αװ��
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'csrf': 'RUJ53PGJ4ZD',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
}

dir_name = '��������'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# �ú�����ȡ������mp3�ļ�
def get_music_mp3(rid, name):
    url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1577081015618&reqId=f4af2221-2549-11ea-92dc-b1e779c8d1d6'.format(
        rid)
    result = requests.get(url, headers=headers).json()
    music_url = result['url']
    with open('��������/{}.mp3'.format(name), 'wb')as f:
        print('��������{}'.format(name), end='')
        music = requests.get(music_url)
        f.write(music.content)
        f.close()
        print('\t�������')


# �ú�������Ÿ�ִ�еĴ����
def main():
    # ���ֵ�����
    singer = str(input('������Ҫ���ظ���:'))
    # ������ҳ��
    number = int(input('������Ҫ���ص�ҳ��:'))
    for x in range(1, number + 1):
        url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&reqId=615ae920-2d21-11ea-b560-73e04c9f8018".format(singer, x)
        response = requests.get(url, headers=headers)
        html = response.text
        result = json.loads(html)
        data = result['data']['list']
        for i in data:
            rid = i['rid']
            name = i['name']
            get_music_mp3(rid,name)

    main()
