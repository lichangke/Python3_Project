#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   countries.py
@Time    :   2019/04/06 23:42:39
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   处理国家识别码
'''

# here put the import lib

# from pygal.i18n import COUNTRIES 模块已被遗弃 但是现在可以在 pygal_maps_world 插件中找到它  pip3 install pygal_maps_world

from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家， 返回Pygal使用的两个字母的国别码"""
    for country_code in sorted(COUNTRIES.keys()):
        for code, name in COUNTRIES.items():
            if name == country_name:
                return code

        # 如果没有找到指定的国家， 就返回None
        return None

