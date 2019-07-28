"""为应用程序users定义URL模式"""

# 非 from django.conf.urls import url
from django.urls import path,re_path
from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import login  In django-2.1, the old function-based views have been removed,

from . import views

app_name= 'users'# 不能少

urlpatterns = [
    # 登录页面
    # re_path(r'^login/$', login, {'template_name': 'users/login.html'},name='login'),
    re_path(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    # 注销
    re_path(r'^logout/$', views.logout_view, name='logout'),

    # 注册页面
    re_path(r'^register/$', views.register, name='register'), # 与URL http://localhost:8000/users/register/匹配， 并将请求发送给我们即将编写的函数register()
]