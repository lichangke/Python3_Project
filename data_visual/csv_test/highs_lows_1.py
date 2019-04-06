#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   highs_lows.py
@Time    :   2019/04/06 22:32:59
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   处理CSV文件
'''

# here put the import lib

#c sv 模块包含在Python标准库中
import csv

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    # 创建一个与该文件相关联的阅读器（reader ） 对象
    reader = csv.reader(f)
    # 模块csv 包含函数next() ， 调用它并将阅读器对象传递给它时， 它将返回文件中的下一行。 在前面的代码中， 我们只调用了next() 一次， 因此得到的是文件的第一行， 其中包含文件头
    header_row = next(reader) 
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

        