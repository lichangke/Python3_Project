from urllib import request
import random, socket,urllib
'''
requests库的基本使用
requests ：https://2.python-requests.org//zh_CN/latest/user/quickstart.html
HTTP头部信息的模拟
'''
# https://docs.python.org/zh-cn/3/library/random.html
url = 'http://httpbin.org/get'
user_agent_list = [ "My user agent 01", "My user agent 02", "My user agent 03","My user agent 04"]
for i in range(5):
    req = request.Request(url=url, headers={"User-Agent": random.choice(user_agent_list)}, method='GET')
    try:
        response = request.urlopen(req,timeout=5)
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')



