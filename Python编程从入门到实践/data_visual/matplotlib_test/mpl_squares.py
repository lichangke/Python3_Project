#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mpl_squares.py
@Time    :   2019/04/06 16:45:51
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   绘制折线图
'''
# here put the import lib
# 导入了模块pyplot 

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5] # X 轴数据

squares = [1, 4, 9, 16, 25] # Y 轴数据
'''
plot(*args[, scalex, scaley, data])
绘制 x y 坐标组成的线
'''
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题， 并给坐标轴加上标签
plt.title( "Square Numbers", fontsize = 24 )
plt.xlabel( "Value", fontsize = 14 )
plt.ylabel( "Square of Value", fontsize = 14 )

# 设置刻度标记的大小
plt.tick_params( axis = 'both', labelsize = 14 , colors = 'r' ) # axis 将参数应用于哪个轴

plt.show()  
'''
打开matplotlib查看器， 并显示绘制的图形
'''
