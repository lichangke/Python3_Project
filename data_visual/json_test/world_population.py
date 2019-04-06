#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   world_population.py
@Time    :   2019/04/06 23:36:41
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   处理JSON格式
'''

# here put the import lib

''' 导入画地图的模块 '''
import pygal.maps.world

''' 解析json文件 '''
import json

'''世界地图的样式'''
import pygal
from pygal.style import RotateStyle  # 十六进制颜色
from pygal.style import LightColorizedStyle # 加亮地图的颜色

from country_codes import get_country_code


# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # population = int(pop_dict['Value']) # '1127437398.85751'  Python不能直接将包含小数点的字符串'1127437398.85751' 转换为整数
        # 先将字符串转换为浮点数， 再将浮点数转换为整数：
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():

    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
    
'''
class pygal.style.RotateStyle(color, step=10, max_=None, base_style=None, **kwargs)
    Create a style by rotating the given color
'''
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle) # 十六进制颜色码 
# wm = pygal.Worldmap()  # 已不可用 使用.maps.world.World()替代
wm = pygal.maps.world.World()  # 初始化一个地图对象
wm.style = wm_style # 设置地图的风格
wm.title = 'World Population in 2010, by Country'
#wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
