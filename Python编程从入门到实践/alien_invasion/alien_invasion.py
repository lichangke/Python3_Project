#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   alien_invasion.py
@Time    :   2019/03/30 22:41:55
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   
主文件alien_invasion.py创建一系列整个游戏都要用到的对象： 存储在ai_settings 中的设置、 存储在screen 中的主显示surface以及一个飞船实例。 
文件alien_invasion.py还包含游戏的主循环， 这是一个调用check_events() 、 ship.update() 和update_screen() 的while 循环。
'''

# here put the import lib
# 导入了模块sys 和pygame
import sys

# 模块pygame 包含开发游戏所需的功能
import pygame

# 导入设置
from settings import Settings

# 导入飞船
from ship import Ship

# # 导入 Alien
# from alien import Alien

# 导入功能函数模块 在模块game_functions 而不是run_game() 中完成大部分工作。
import game_functions as gf

# pygame.sprite.Group 类类似于列表，但提供了有助于开发游戏的额外功能
# 用于存储所有有效的子弹， 以便能够管理发射出去的所有子弹。
from pygame.sprite import Group

# 导入 GameStats 跟踪游戏统计信息
from game_stats import GameStats

# 导入按钮
from button import Button

# 导入Scoreboard 用于 创建记分牌
from scoreboard import Scoreboard

# pygame 文档 https://www.pygame.org/docs/ref/pygame.html


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # ide 可能会误报 不存在
    ai_settings = Settings()  # 设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # 屏幕大小  默认创建一个黑色屏幕

    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一个Scoreboard 实例
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)  # 入参 包括屏幕 和 设置 信息

    # 创建一个用于存储子弹的编组
    # 创建了一个Group 实例， 并将其命名为bullets 。 这个编组是在while 循环外面创建的， 这样就无需每次运行该循环时都创建一个新的子弹
    bullets = Group()
    aliens = Group()
    # # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship,aliens)

    # 开始游戏的主循环
    while True:

        # 监视键盘鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets)

        # 仅在游戏处于活动状态时才运行
        if stats.game_active:
            # 每次执行循环时都调用飞船的方法update() 根据标志 更新飞船位置 通过绘制实现移动
            ship.update()
            # 子弹更新
            gf.update_bullets(ai_settings, screen, stats, sb, ship,aliens, bullets)

            print(len(bullets))

            # 更新每个外星人的位置
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,bullets)
        # 绘制更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button)


run_game()
