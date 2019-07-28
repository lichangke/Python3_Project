#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2019/03/30 23:02:53
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   每次给游戏添加新功能时， 通常也将引入一些新设置 要修改游戏， 只需修改
settings.py中的一些值， 而无需查找散布在文件中的不同设置。
文件settings.py包含Settings 类， 这个类只包含方法__init__() ， 它初始化控制游戏外观和飞船速度的属性。
'''

# here put the import lib


class Settings():
    """存储《外星人入侵》 的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5  # 速度
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3  # 限制子弹数目

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10  # fleet_drop_speed 指定了有外星人撞到屏幕边缘时， 外星人群向下移动的速度
        # fleet_direction为1表示向右移， 为-1表示向左移
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()  # 设置speedup_scale ， 用于控制游戏节奏的加快速度2 表示玩家每提高一个等级， 游戏的节奏就翻倍； 1表示游戏节奏始终不变。

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右； 为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
