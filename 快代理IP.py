# coding=gbk
import requests
import parsel
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_content(url):
    response = requests.get(url, headers=headers).text
    parse = parsel.Selector(response)
    contents = parse.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    proxies_list = []
    for content in contents:
        dict_proxies = {}
        type = content.xpath('.//td[4]/text()').extract_first()
        IP = content.xpath('.//td[1]/text()').extract_first()
        port = content.xpath('.//td[2]/text()').extract_first()
        dict_proxies[type] = IP + ':' + port
        print(dict_proxies)
        proxies_list.append(dict_proxies)

    #print(proxies_list)


if __name__ == '__main__':
    urls = ['https://www.kuaidaili.com/free/inha/{}'.format(i) for i in range(3, 5)]
    for url in urls:
        print(url)
        get_content(url)
