# coding=gbk
import jieba.analyse
import requests
import re
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
url = 'https://m.weibo.cn/comments/hotflow?id=4465494835252808&mid=4465494835252808&max_id_type=0'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36'
}
response = requests.get(url, headers=headers)
data = json.loads(response.content.decode())
# print(data)
# pprint.pprint(data)
res = data['data']['data']
# print(res)
# print(len(res))
for i in range(0, len(res)):
    r = res[i]['text']
    # print(r)
    info = ''.join(re.findall('[\u4e00-\u9fa5]', r))
    #print(info)
    with open(r'C:\Users\Lenovo-PC\Desktop\猫眼电影\weibo.txt', 'a+') as f:
        f.write(info + '\n')
        f.close()

path = r'C:\Users\Lenovo-PC\Desktop\猫眼电影\weibo.txt'
fp = open(path, 'r')
content = fp.read()
try:
    jieba.analyse.set_stop_words(r'C:\Users\Lenovo-PC\Desktop\呆萌的停用词表.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for item in tags:
        print(item[0] + '\t' + str(int(item[1] * 1000)))
finally:
    fp.close()
