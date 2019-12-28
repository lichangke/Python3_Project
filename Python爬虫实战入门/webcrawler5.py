import requests
import re

'''
requests库的基本使用
requests ：https://2.python-requests.org//zh_CN/latest/user/quickstart.html
正则表达式
re：https://docs.python.org/zh-cn/3/library/re.html
匹配网页所需信息

获取 https://book.douban.com/top250 页面 25本书的书名
'''

url = "https://book.douban.com/top250"
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
headers = {"User-Agent": user_agent}
# 有做拦击，需要传入 headers - user_agent
content = requests.get(url, headers=headers).text
'''
re.S
re.DOTALL
让 '.' 特殊字符匹配任何字符，包括换行符；如果没有这个标记，'.' 就匹配 除了 换行符的其他任意字符。对应内联标记 (?s) 。
'''
pattern = re.compile(r'<a href=.*?title="(.*?)"', re.S)
results = re.findall(pattern, content)
length = len(results)
count = length if length <= 25 else 25
for index in range(count):
    name = results[index]
    print("{}:《{}》".format(index+1, name))
