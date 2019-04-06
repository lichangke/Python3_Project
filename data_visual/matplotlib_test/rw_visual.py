import matplotlib.pyplot as plt
from random_walk import RandomWalk


# 只要程序处于活动状态， 就不断地模拟随机漫步
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    '''
    figure([num, figsize, dpi, facecolor, ...])
        Create a new figure.
        figsize : (float, float), optional, default: None
            width, height in inches. If not provided, defaults to rcParams["figure.figsize"] = [6.4, 4.8].
        dpi : integer, optional, default: None
            resolution of the figure. If not provided, defaults to rcParams["figure.dpi"] = 100.
    '''
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6),dpi=128)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none')

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors='none', s=100)

    '''
    The Axes class The Axes contains most of the figure elements: Axis, Tick, Line2D, Text, Polygon, etc., and sets the coordinate system.
    '''
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)   # Return the XAxis instance.
    plt.axes().get_yaxis().set_visible(False)   # Return the YAxis instance.

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
