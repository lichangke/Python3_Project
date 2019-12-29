

GitHub link [Python爬虫实战入门](https://github.com/lichangke/Python3_Project/tree/master/Python%E7%88%AC%E8%99%AB%E5%AE%9E%E6%88%98%E5%85%A5%E9%97%A8)
### 1.urllib 简单使用演示
urllib 参看 [https://docs.python.org/zh-cn/3/library/urllib.html](https://docs.python.org/zh-cn/3/library/urllib.html)

webcrawler.py
```python
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
```

### 2.HTTP头部信息的模拟

webcrawler2.py
```python
import random, socket,urllib
'''
HTTP头部信息的模拟
'''
# https://docs.python.org/zh-cn/3/library/random.html
url = 'http://httpbin.org/get'
user_agent_list = [ "My user agent 01", "My user agent 02", "My user agent 03","My user agent 04"]
for i in range(5):
    req = urllib.request.Request(url=url, headers={"User-Agent": random.choice(user_agent_list)}, method='GET')
    try:
        response = urllib.request.urlopen(req,timeout=5)
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')
```

### 3.requests库的基本使用
requests 参看 [https://2.python-requests.org//zh_CN/latest/user/quickstart.html](https://2.python-requests.org//zh_CN/latest/user/quickstart.html)

webcrawler3.py
```python
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
```

webcrawler4.py
```python
# get请求
import requests

'''
requests库的基本使用
requests ：https://2.python-requests.org//zh_CN/latest/user/quickstart.html
'''

url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
# .get是使用get方式请求url，字典类型的data不用进行额外处理
response = requests.get(url, data)
print(response.text)


# post请求
import requests
url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz'}
# .post表示为post方法
response = requests.post(url, data)
# 返回类型为json格式
print(response.json())
```

### 4.正则匹配网页所需信息
re 参见 [https://docs.python.org/zh-cn/3/library/re.html](https://docs.python.org/zh-cn/3/library/re.html)
**获取[https://book.douban.com/top250](https://book.douban.com/top250)  豆瓣 top 25 书籍的信息**

webcrawler5.py
```python
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
```

### 5.BeautifulSoup 获取网页信息

Beautiful Soup 参看 [https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
#### 获取 [https://book.douban.com/top250](https://book.douban.com/top250)  豆瓣 top 25 书籍的信息

webcrawler6.py
```python
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
```

#### 获取 [https://book.douban.com/top250](https://book.douban.com/top250)  豆瓣 top 250 书籍的信息并保存 单线程
Python I/O参看 [https://docs.python.org/zh-cn/3/library/io.html](https://docs.python.org/zh-cn/3/library/io.html)

webcrawler7.py
```python
import requests
from bs4 import BeautifulSoup
import time
'''
Beautiful Soup 使用
Beautiful Soup：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
Python I/O：https://docs.python.org/zh-cn/3/library/io.html
获取 https://book.douban.com/top250 top250的书本信息
'''
def get_data_from_web(url):
    """
    获取url链接中书本信息
    :param url: 链接
    :return: books_list 此url中书本信息列表 eg: [{'href': 'https://book.douban.com/subject/1770782/', 'book': '追风筝的人', 'author': '[美] 卡勒德·胡赛尼 '}]
    """
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    headers = {"User-Agent": user_agent}
    # 有做拦击，需要传入 headers - user_agent
    content = requests.get(url, headers=headers).text
    # 关于 "lxml" 见 https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id9
    soup = BeautifulSoup(content, "lxml")
    table_list = soup.find(id="wrapper").find(class_="indent").find_all("table")
    # table_list 每个元素存储的是一本书的信息
    books_list = list()
    for table in table_list:
        book_dict = dict()
        book_dict["href"] = table.find(class_="pl2").a.get("href")
        book_dict["name"] = table.find(class_="pl2").a.get("title")
        book_dict["author"] = table.find(class_="pl").string.split("/")[0]
        books_list.append(book_dict)
    return books_list
def save_data(books_data,save_name):
    """
    将书本信息保存到 save_name 文件中
    :param books_data:  书本信息
    :param save_name: 文件名
    """
    # https://docs.python.org/zh-cn/3/library/io.html
    with open(save_name, 'w', encoding='utf-8') as f:
        index = 0
        for book in books_data:
            index += 1
            f.write("{:0>3}:《{}》作者:{} {}\r".format(index, book.get("name"),book.get("author"),book.get("href")))
if __name__ == '__main__':
    top250_books_info = list()
    start_time = time.perf_counter()
    for i in range(10):
        url = "https://book.douban.com/top250?start={}".format(i*25)
        books_info = get_data_from_web(url)
        top250_books_info.extend(books_info)
    end_time = time.perf_counter()
    print('Cost {} seconds'.format(end_time - start_time))
    save_name = "top250Booksinfo.txt"
    save_data(top250_books_info,save_name)

```
单线程读取网页信息耗时： Cost 5.144416238 seconds

#### 获取 [https://book.douban.com/top250](https://book.douban.com/top250)  豆瓣 top 250 书籍的信息并保存 多线程

futures 使用 参见 [https://blog.csdn.net/leacock1991/article/details/101467226](https://blog.csdn.net/leacock1991/article/details/101467226)

webcrawler8.py
```python
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import threading
import time
'''
Beautiful Soup 使用
Beautiful Soup：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
Python I/O：https://docs.python.org/zh-cn/3/library/io.html
获取 https://book.douban.com/top250 top250的书本信息
多线程版
futures 使用参见 https://blog.csdn.net/leacock1991/article/details/101467226
'''
def get_data_from_web(url):
    """
    获取url链接中书本信息
    :param url: 链接
    :return: books_list 此url中书本信息列表 eg: [{'href': 'https://book.douban.com/subject/1770782/', 'book': '追风筝的人', 'author': '[美] 卡勒德·胡赛尼 '}]
    """
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    headers = {"User-Agent": user_agent}
    # 有做拦击，需要传入 headers - user_agent
    content = requests.get(url, headers=headers).text
    # 关于 "lxml" 见 https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id9
    soup = BeautifulSoup(content, "lxml")
    table_list = soup.find(id="wrapper").find(class_="indent").find_all("table")
    # table_list 每个元素存储的是一本书的信息
    books_list = list()
    for table in table_list:
        book_dict = dict()
        book_dict["href"] = table.find(class_="pl2").a.get("href")
        book_dict["name"] = table.find(class_="pl2").a.get("title")
        book_dict["author"] = table.find(class_="pl").string.split("/")[0]
        books_list.append(book_dict)
    with lock:
        top250_books_info.extend(books_list)
def save_data(books_data,save_name):
    """
    将书本信息保存到 save_name 文件中
    :param books_data:  书本信息
    :param save_name: 文件名
    """
    # https://docs.python.org/zh-cn/3/library/io.html
    with open(save_name, 'w', encoding='utf-8') as f:
        index = 0
        for book in books_data:
            index += 1
            f.write("{:0>3}:《{}》作者:{} {}\r".format(index, book.get("name"),book.get("author"),book.get("href")))
lock = threading.Lock()
top250_books_info = list()
if __name__ == '__main__':
    urls_list = list()
    start_time = time.perf_counter()
    for i in range(10):
        url = "https://book.douban.com/top250?start={}".format(i*25)
        urls_list.append(url)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_data_from_web, urls_list)
    end_time = time.perf_counter()
    print('Cost {} seconds'.format( end_time - start_time))
    # 没有按顺序读取网页信息
    save_name = "top250Booksinfo_mult.txt"
    save_data(top250_books_info,save_name)
```
多线程读取网页信息耗时： Cost 0.8504998400000001 seconds

### 6.BeautifulSoup 下载网页图片
requests 参见 [ https://2.python-requests.org//zh_CN/latest/user/quickstart.html]( https://2.python-requests.org//zh_CN/latest/user/quickstart.html)
Beautiful Soup 参见 [https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
Python I/O 参见 [https://docs.python.org/zh-cn/3/library/io.html](https://docs.python.org/zh-cn/3/library/io.html)
错误和异常  参见 [https://docs.python.org/zh-cn/3/tutorial/errors.html](https://docs.python.org/zh-cn/3/tutorial/errors.html)
shutil:参见  [https://docs.python.org/3/library/shutil.html](https://docs.python.org/3/library/shutil.html)
        参见  [ https://blog.csdn.net/qq_38640439/article/details/81410116]( https://blog.csdn.net/qq_38640439/article/details/81410116)

获取 下载 [https://pixabay.com/zh/images/search/?pagi=1](https://pixabay.com/zh/images/search/?pagi=1) 图片

多线程版
futures 使用参见 [https://blog.csdn.net/leacock1991/article/details/101467226](https://blog.csdn.net/leacock1991/article/details/101467226)

webcrawler9.py
```python
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time
import os
import shutil

'''

requests ：https://2.python-requests.org//zh_CN/latest/user/quickstart.html
Beautiful Soup：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
Python I/O：https://docs.python.org/zh-cn/3/library/io.html
错误和异常：https://docs.python.org/zh-cn/3/tutorial/errors.html
shutil: https://docs.python.org/3/library/shutil.html
        https://blog.csdn.net/qq_38640439/article/details/81410116

获取 下载 https://pixabay.com/zh/images/search/?pagi=1 图片
多线程版
futures 使用参见 https://blog.csdn.net/leacock1991/article/details/101467226
'''

def download_save_pic(img_url,img_path):
    # stream 属性 可参见 流式请求 https://2.python-requests.org//zh_CN/latest/user/advanced.html#streaming-requests
    # 响应体内容工作流 https://2.python-requests.org//zh_CN/latest/user/advanced.html#body-content-workflow
    # 在请求中把 stream 设为 True，Requests 无法将连接释放回连接池，除非你 消耗了所有的数据，或者调用了 Response.close。
    with requests.get(img_url, stream=True) as response:  # stream=True，以使requests不会首先将整个图像下载到内存中
        if response.status_code == 200:
            with open(img_path, 'wb') as f:  # 写入 二进制模式
                response.raw.decode_content = True # 设置为 True的原因 见 关于python：如何使用请求下载图像 https://www.codenong.com/13137817/
                # 将文件内容拷贝到另一个文件中, 注意与其他 copy函数区别
                shutil.copyfileobj(response.raw, f)
        else:
            print("开始下载 {} 出问题".format(img_url))

def download_pic_from_web(url_index):
    url = url_index[0]
    index = url_index[1]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    headers = {"User-Agent": user_agent}
    # 有做拦击，需要传入 headers - user_agent
    try:
        response = requests.get(url, headers=headers, time = 3)
    except requests.Timeout as e:
        print('Catch TIME OUT: Get {}'.format(url))

    soup = BeautifulSoup(response.text, 'lxml')
    picture_items = soup.find(class_='flex_grid credits search_results').find_all('div', class_='item')   # 所有图片
    for picture_item in picture_items:
        imgurl = picture_item.find('img').get('src')
        if -1 == imgurl.find('https:'):     # 不是链接找其他
            imgurl = picture_item.find('img').get('data-lazy')
        dir = os.path.abspath('.\pic{}'.format(index))  # 当前路径的绝对路径
        if not os.path.exists(dir):
            os.makedirs(dir)    # 文件不存在建立
        # 提取网页链接中图片 eg: https://cdn.pixabay.com/photo/2019/12/24/05/59/butterfly-4716054__340.jpg 中的 butterfly-4716054__340.jpg
        filename = os.path.basename(imgurl)
        imgpath = os.path.join(dir,filename)    # 保存图片的绝对路径
        print('开始下载 thread{} : {}'.format(index, imgurl))
        try:
            download_save_pic(imgurl, imgpath)
        except requests.exceptions.MissingSchema:   # 链接有问题跳过
            print("catch requests.exceptions.MissingSchema")
            continue


if __name__ == '__main__':

    urls_list = list()
    start_time = time.perf_counter()
    for i in range(1, 5):
        url = "https://pixabay.com/zh/images/search/?pagi={}".format(i)
        urls_list.append([url, i])
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_pic_from_web, urls_list)
    end_time = time.perf_counter()
    print('Cost {} seconds'.format(end_time - start_time))
```

----
>*GitHub链接：*
>*[https://github.com/lichangke/LeetCode](https://github.com/lichangke/LeetCode)*
>*CSDN首页：*
>*[https://me.csdn.net/leacock1991](https://me.csdn.net/leacock1991)*
>*欢迎大家来一起交流学习*
