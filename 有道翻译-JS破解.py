# coding=gbk
import hashlib
import random
import requests, time
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

appVersion = '5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'


def make_MD5(word):
    # 5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
    result = hashlib.md5(word.encode())
    return result.hexdigest()


def requests_shuju(url, e):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '243',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-284607051@10.108.160.18; JSESSIONID=aaaQ1C-00rFt29rZbtCex; OUTFOX_SEARCH_USER_ID_NCOO=1467546057.7762415; ___rl__test__cookies=1585317700221',
        'DNT': '1',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    ts = str(int(time.time() * 1000))
    i = ts + str(random.randint(0, 9))
    sign = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
    data = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': i,
        'sign': make_MD5(sign),
        'ts': ts,
        'bv': make_MD5(appVersion),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    response = requests.post(url, data=data, headers=headers).json()
    res = response['translateResult']
    print(res)


if __name__ == '__main__':
    e = input("请输入英文：")
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    requests_shuju(url, e)
