import requests
from bs4 import BeautifulSoup

'''
Beautiful Soup 使用
Beautiful Soup：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

获取 https://book.douban.com/top250 页面 25本书的书名
'''

url = "https://book.douban.com/top250"
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
headers = {"User-Agent": user_agent}
# 有做拦击，需要传入 headers - user_agent
content = requests.get(url, headers=headers).text
# 关于 "lxml" 见 https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id9
soup = BeautifulSoup(content,"lxml")
wrapper_content_a_list = soup.find(id="wrapper").find(id="content").find_all("a")
index = 0
for result in wrapper_content_a_list:
    name = result.get("title")
    link = result.get("href")
    if name is not None:
        index += 1
        print("{}:《{}》{}".format(index, name, link))

