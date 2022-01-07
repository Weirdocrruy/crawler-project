# coding = gbk
# -*- coding:utf-8 -*-
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

url = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/AvCReLikjzYEf9XjTQxbv3JWgKT.jpg'
response = requests.get(url)
print(response.content)
file_name1 = url.split('/')[-1]

# 保存
with open('img\\' + file_name1, 'wb')as f:
    print('正在保存:', file_name1)
    f.write(response.content)
