#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scatter_squares.py
@Time    :   2019/04/06 17:08:01
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   绘制散点图
'''

# here put the import lib
import matplotlib.pyplot as plt

'''
scatter(x, y[, s, c, marker, cmap, norm, ...])
绘制x y 坐标的散点图，并设置不同的 标记 大小 或 颜色等。
'''

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
color = ['r', 'g', 'b']

# s 标记大小 以磅为单位**2  c 颜色，序列或颜色序列
plt.scatter(x_values, y_values, s=100, c=color)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


# 循环绘制1000个点

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]


'''
c : color, sequence, or sequence of color, optional
    A single color format string.
    A sequence of color specifications of length n.
    A sequence of n numbers to be mapped to colors using cmap and norm.  #使用cmap和norm映射到颜色的n个数字序列
    A 2-D array in which the rows are RGB or RGBA.

cmap : Colormap, optional, default: None  # cmap 告诉pyplot 使用哪个颜色映射

edgecolors : color or sequence of color, optional, default: 'face' # 边框颜色

'''

plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Blues, edgecolor='none')

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

'''
axis(*v, **kwargs)
获取或设置某些轴属性的便捷方法
xmin, xmax, ymin, ymax = axis()
xmin, xmax, ymin, ymax = axis(xmin, xmax, ymin, ymax)
xmin, xmax, ymin, ymax = axis(option)
xmin, xmax, ymin, ymax = axis(**kwargs)
'''
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
