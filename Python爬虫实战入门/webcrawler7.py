import requests
from bs4 import BeautifulSoup

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
    for i in range(10):
        url = "https://book.douban.com/top250?start={}".format(i*25)
        books_info = get_data_from_web(url)
        top250_books_info.extend(books_info)
    save_name = "top250Booksinfo.txt"
    save_data(top250_books_info,save_name)
