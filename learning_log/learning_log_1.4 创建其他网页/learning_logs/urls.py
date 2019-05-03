"""定义learning_logs的URL模式"""
from django.urls import path,re_path
from . import views

app_name='learning_logs' # 不能少 ，否则runserver的时候就会出错

# https://docs.djangoproject.com/en/2.2/ref/urls/#module-django.urls.conf
urlpatterns = [
    # 主页
    path('', views.index, name='index'),    # Django将在文件views.py中查找函数index()

    # 显示所有的主题
    path('topics/',views.topics,name = 'topics'),

    # 特定主题的详细页面
    # use a regular expression, you can use re_path(). https://stackoverflow.com/questions/47661536/django-2-0-path-error-2-0-w001-has-a-route-that-contains-p-begins-wit
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), # ?P<topic_id> 将匹配的值存储到topic_id 中； 而表达式\d+ 与包含在两个斜杆内的任何数字都匹配， 不管这个数字为多少位。
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