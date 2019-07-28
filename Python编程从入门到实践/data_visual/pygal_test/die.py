#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   die.py
@Time    :   2019/04/06 21:53:11
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   骰子类
'''

# here put the import lib

from random import randint


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
        '''
        def randint(a, b)
            Return random integer in range [a, b], including both end points.
        '''
