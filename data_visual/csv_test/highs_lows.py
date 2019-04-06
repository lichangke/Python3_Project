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

# c sv 模块包含在Python标准库中
import csv

from matplotlib import pyplot as plt
# 模块datetime 处理日期
from datetime import datetime

# 从文件中获取日期、 最高气温和最低气温
filename = 'death_valley_2014.csv'

with open(filename) as f:
        # 创建一个与该文件相关联的阅读器（reader ） 对象
    reader = csv.reader(f)
    # 模块csv 包含函数next() ， 调用它并将阅读器对象传递给它时， 它将返回文件中的下一行。 在前面的代码中， 我们只调用了next() 一次， 因此得到的是文件的第一行， 其中包含文件头
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:  # 遍历文件中余下的各行
        try: # 错误检查
            current_date = datetime.strptime(row[0], "%Y-%m-%d")  # '2014-7-1
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high) 
            lows.append(low)


# 根据数据绘制图形
fig = plt.figure(dpi=123, figsize=(10, 6))

'''
plot(*args[, scalex, scaley, data])
    Plot y versus x as lines and/or markers.
        alpha: float  Set the alpha value used for blending - not supported on all backends.
'''
plt.plot(dates, highs, c='red', alpha=0.5)  # 绘制最高温度
plt.plot(dates, lows, c='blue', alpha=0.5)  # 绘制最低温度

'''
fill_between(x, y1[, y2, where, ...])
    Fill the area between two horizontal curves.
'''
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
'''
autofmt_xdate(self, bottom=0.2, rotation=30, ha='right', which=None)
    Date ticklabels often overlap, so it is useful to rotate them and right align them.
    bottom : scalar
        The bottom of the subplots for subplots_adjust().
    rotation : angle in degrees
        The rotation of the xtick labels.
    ha : string
        The horizontal alignment of the xticklabels.
    which : {None, 'major', 'minor', 'both'}
        Selects which ticklabels to rotate. Default is None which works the same as major.


'''
fig.autofmt_xdate()

title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=24)

'''
tick_params([axis])
    Change the appearance of ticks, tick labels, and gridlines. 更改刻度，刻度标签和网格线的外观
    axis : {'x', 'y', 'both'}, optional
        Which axis to apply the parameters to.
    which : {'major', 'minor', 'both'}
        Default is 'major'; apply arguments to which ticks.
'''
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
