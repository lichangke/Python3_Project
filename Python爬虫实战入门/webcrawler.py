

from urllib import request   # 打开和读取 URL
from urllib import parse    # 用于解析 URL

'''
urllib 简单使用演示
urllib： https://docs.python.org/zh-cn/3/library/urllib.html
'''

# 演示 request 打开和读取 URL
url = 'http://www.baidu.com'
response = request.urlopen(url,timeout=1)
print(response.read().decode('utf-8'))

# 演示 post 和 get
response2 = request.urlopen('http://httpbin.org/get',timeout=10)
print(response2.read().decode('utf-8'))

data = bytes(parse.urlencode({'world':'hello'}),encoding='utf-8')
response1 = request.urlopen('http://httpbin.org/post',data = data)
print(response1.read().decode('utf-8'))

import urllib
import socket
try:
    response3 = request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.request.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

try:
    response4 = request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

