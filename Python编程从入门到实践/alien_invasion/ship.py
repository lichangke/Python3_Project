#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ship.py
@Time    :   2019/03/30 23:09:54
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   飞船信息
文件ship.py包含Ship 类， 这个类包含方法__init__() 、 管理飞船位置的方法update() 以及在屏幕上绘制飞船的方法blitme() 。
 表示飞船的图像存储在文件夹images下的文件ship.bmp中。
'''

# here put the import lib
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        
        self.screen = screen  # 屏幕数据
        self.ai_settings = ai_settings  # 设置
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        # 在Pygame中， 原点(0, 0)位于屏幕左上角， 向右下方移动时， 坐标值将增大
        self.rect.centerx = self.screen_rect.centerx  #每次飞船移动 只是 rect.centerx 改变  rect.bottom 不变
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志  玩家按住右箭头键不放时， 我们希望飞船不断地向右移动， 直到玩家松开为止 让游戏检测pygame.KEYUP 事件然
        # 后， 我们将结合使用KEYDOWN 和KEYUP 事件， 以及一个名为moving_right 的标志来实现持续移动
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值， 而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right: # 限制右边界
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0: # 限制左边界
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center  #self.rect.centerx 将只存储self.center 的整数部分， 但对显示飞船而言， 这问题不大

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
