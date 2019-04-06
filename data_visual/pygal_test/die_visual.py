#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   die_visual.py
@Time    :   2019/04/06 21:56:06
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   模拟掷骰子
'''

# here put the import lib

from die import Die

import pygal

# 创建两个D6
die_1 = Die(8)
die_2 = Die(8)

# 掷几次骰子， 并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll()+die_2.roll()
    results.append(result)


# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()  # Basic simple bar graph:

hist.title = "Results of rolling a D6 and a D10 50,000  times."
x_labels = set()
for i in range(1,die_1.num_sides+1):
    for j in range(1, die_2.num_sides+1):
        x_label = i + j
        x_labels.add(x_label)

print(x_labels)

hist.x_labels = list(x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# 使用add() 将一系列值添加到图表中（向它传递要给添加的值指定的标签， 还有一个列表， 其中包含将出现在图表中的值） 。
hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')  # 最后， 我们将这个图表渲染为一个SVG文件
