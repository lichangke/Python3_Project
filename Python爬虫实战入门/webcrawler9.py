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
        except requests.exceptions.MissingSchema:   #  链接有问题跳过
            print("catch requests.exceptions.MissingSchema")
            continue


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

