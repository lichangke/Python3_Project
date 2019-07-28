#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   game_stats.py
@Time    :   2019/03/31 01:11:49
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   None
'''

# here put the import lib

#在这个游戏运行期间， 我们只创建一个GameStats 实例， 但每当玩家开始新游戏时， 需要重置一些统计信息。
#我们在方法reset_stats() 中初始化大部分统计信息，而不是在__init__() 中直接初始化它们。 
class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏一开始处于非活动状态 单击Play按钮来开始游戏
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1