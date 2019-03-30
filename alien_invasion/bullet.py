#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bullet.py
@Time    :   2019/03/30 23:56:20
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   None
'''

# here put the import lib
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        # 了解 super 可参见  https://www.jianshu.com/p/6b79d13fcff5
        super(Bullet, self).__init__()  # 在super机制里可以保证公共父类仅被执行一次
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形， 再设置正确的位置
        # 子弹并非基于图像的， 因此我们必须使用pygame.Rect() 类从空白开始创建一个矩形。
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 正确的位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    # 位置更新
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
    # 绘制子弹
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
