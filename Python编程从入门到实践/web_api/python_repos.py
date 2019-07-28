#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_repos.py
@Time    :   2019/04/26 23:01:12
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   None
'''

# here put the import lib
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pygal
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

result = requests.get(url)

print("Status code:", result.status_code)

# 将API响应存储在一个变量中
response_dict = result.json()
print("Total repositories:", response_dict['total_count'])
# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

print("\nSelected information about first repository:")

names, stars, plot_dicts = [], [], []
# 遍历仓库提取数据
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    stars.append(repo_dict['stargazers_count'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
    # 规避 由于网络原因部分未获取到时，plot_dict 为 None，导致 chart.render_to_file('python_repos.svg') 报错 AttributeError: 'NoneType' object has no attribute 'decode'
    if not repo_dict['stargazers_count']:
        repo_dict['stargazers_count'] = "None"
        breakpoint() # 注 此内置函数 New in version 3.7.+
    if not repo_dict['description'] :
        repo_dict['description'] = "None"
        breakpoint()
    if not repo_dict['html_url']:
        repo_dict['html_url'] = "None"
        breakpoint()

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }  # 注意最后有 逗号
    plot_dicts.append(plot_dict)

# 可视化
mystyle = LS('#333366', base_style=LCS)


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=mystyle)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)

chart.render_to_file('python_repos.svg')
