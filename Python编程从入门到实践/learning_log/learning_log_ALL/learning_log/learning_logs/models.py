#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2019/04/28 22:23:15
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   我们导入了模块models， 还让我们创建自己的模型。 模型告诉Django如何处理应用程序中存储的数据。 在代码层面， 模型就是一个类，  包含属性
和方法。 
'''

# here put the import lib

from django.db import models
from django.contrib.auth.models import User # 导入了django.contrib.auth 中的模型User ， 然后在Topic 中添加了字段owner ， 它建立到模型User 的外键关系

# Create your models here. # 在这里创建模型
# 创建了一个名为Topic 的类， 它继承了Model ——Django中一个定义了模型基本功能的类。
class Topic(models.Model):
    ''' 用户学习的主题'''
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#charfield
    text = models.CharField(max_length = 200) # 属性text是一个CharField——由字符或文本组成的数据
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#datetimefield
    date_added = models.DateTimeField(auto_now_add=True) # 实参auto_add_now=True 让Django将这个属性自动设置成当前日期和时间。
    owner = models.ForeignKey(User,on_delete=models.CASCADE) # 
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

# Entry 也继承了Django基类Model
class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    # 外键是一个数据库术语， 它引用了数据库中的另一条记录； 这些代码将每个条目关联到特定的主题。 每个主题创建时， 都给它分配了一个键（或ID） 。 
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#foreignkey
    # 注 在django2.0后定义外键和一对一关系的时候需要加on_delete选项
    topic = models.ForeignKey("Topic",on_delete=models.CASCADE)
    '''
    书中源代码：
        topic = models.ForeignKey(Topic)
    应改为：
        topic = models.ForeignKey("Topic",on_delete=models.CASCADE)
    '''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # 在Entry 类中嵌套了Meta 类。 Meta 存储用于管理模型的额外信息， 在这里， 它让我们能够设置一个特殊属性， 让Django在需要时使用Entries 来表示多个条目。 
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            return self.text[:50] + "..." # 由于条目包含的文本可能很长， 我们让Django只显示text 的前50个字符
        else:
            return self.text

