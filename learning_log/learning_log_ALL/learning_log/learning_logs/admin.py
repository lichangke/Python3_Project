from django.contrib import admin

# Register your models here. 在这里注册你的模型

from learning_logs.models import Topic,Entry  # 入我们要注册的模型Topic，Entry
admin.site.register(Topic) # 让Django通过管理网站管理我们的模型
admin.site.register(Entry)