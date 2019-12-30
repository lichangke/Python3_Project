import requests
from bs4 import BeautifulSoup
import time


def get_book_info(url):
    """
    获取 url 中书籍以及短评并保存
    :param url:
    :return:
    """
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    headers = {"User-Agent": user_agent}
    # 有做拦击，需要传入 headers - user_agent
    try:
        content = requests.get(url, headers=headers).text
    except requests.Timeout:
        print('TIME OUT: {}'.format(url))
        return
    # BeautifulSoup中各种html解析器的比较及使用 https://blog.csdn.net/Winterto1990/article/details/47806175
    soup = BeautifulSoup(content, "lxml")
    soup.prettify()
    table_list = soup.find(id="wrapper").find(class_="indent").find_all("table")
    for table in table_list:
        href = table.find(class_="pl2").a.get("href")
        book = table.find(class_="pl2").a.get("title")
        auther = table.find(class_="pl").string.split("/")[0]
        get_save_book_comment(book , auther, href)
    return


def get_save_book_comment(book,auther,href):
    """
    获取 书籍短评 并保存
    :param book:
    :param auther:
    :param href:
    :return:
    """
    print("开始获取书籍《{}》的短评".format(book))
    book_info = "\r\n《{}》(豆瓣) 作者:{} -- 链接：{}\r\n".format(book,auther,href)
    comment_url = href+"/comments/"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    headers = {"User-Agent": user_agent}
    try:
        content = requests.get(comment_url, headers=headers).text
    except requests.Timeout:
        print('TIME OUT: {}'.format(url))
        return
    soup = BeautifulSoup(content, "lxml")
    soup.prettify()
    comment_list = soup.find(id="comments").find_all(class_="comment")  # 所有 短评list
    count = 0
    comment_info = str()
    for comment in comment_list:
        count += 1
        if count > 10: break
        name = comment.find(class_="comment-info").a.string
        content = comment.find(class_="comment-content").find(class_="short").string
        content = content.replace("\r","").replace("\n","")
        comment_info += "\t{}.{}\t评论:\t{}\r\n".format(count, name, content)
        print("\t获取 {} 的短评".format(name))
    save_info = book_info + comment_info
    print("获取书籍《{}》的短评结束".format(book))
    save_data(save_info)
    return


def save_data(save_info):
    """
    保存 信息
    :param save_info:
    """
    save_name = "top250BooksCommentinfo.txt"

    with open(save_name, 'a+', encoding='utf-8') as file:
        file.write(save_info)


if __name__ == '__main__':
    start_time = time.perf_counter()
    for i in range(1):
        url = "https://book.douban.com/top250?start={}".format(i*25)
        get_book_info(url)
    end_time = time.perf_counter()
    print('Cost {} seconds'.format(end_time - start_time))
