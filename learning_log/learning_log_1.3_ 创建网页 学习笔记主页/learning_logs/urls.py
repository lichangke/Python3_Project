"""定义learning_logs的URL模式"""
from django.urls import path,re_path
from . import views

app_name='learning_logs' # 不能少 ，否则runserver的时候就会出错

# https://docs.djangoproject.com/en/2.2/ref/urls/#module-django.urls.conf
urlpatterns = [
    # 主页
    path('', views.index, name='index'),    # Django将在文件views.py中查找函数index()
]

# urls -> views -> html  添加网页步骤

'''
Django版本更新,书上的代码需做相应修改

书中源代码：
from django.conf.urls import url
from . import views
urlpatterns = [
     # Home page.
    url(r'^$', views.index, name='index'),

    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]

应改为：
from django.urls import path
from . import views

app_name='learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有的主题
    path('topics/', views.topics, name='topics'),

    # 特定主题的详细页面
    path("topics/(?P<topic_id>\d+)/", views.topic, name='topic'),
]

'''