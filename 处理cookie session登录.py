# coding = gbk
import requests

# »á»°
session = requests.session()
data = {'loginName': '18614075987',
        'password': 'q6035945'}
url = 'https://passport.17k.com/ck/user/login'
session.requests(url, data=data)
resp = session.get('http://user.17k.com/ck/author/shelf?')
print(resp.json())
