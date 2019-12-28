import requests
import random
'''
requests库的基本使用
requests ：https://2.python-requests.org//zh_CN/latest/user/quickstart.html
'''
# https://docs.python.org/zh-cn/3/library/random.html
url = 'http://httpbin.org/get'
user_agent_list = [ "My user agent 01", "My user agent 02", "My user agent 03","My user agent 04"]
for i in range(5):
    try:
        response = requests.get(url=url, headers={"User-Agent": random.choice(user_agent_list)}, timeout=3)
        print(response.text)
    except requests.Timeout as e:
        print('TIME OUT')



