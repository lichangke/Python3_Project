"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 导入了为项目和管理网站管理URL的函数和模块
from django.contrib import admin
from django.urls import path,include
# urlpatterns 包含项目中的应用程序的URL
urlpatterns = [
    path('admin/', admin.site.urls), # 该模块定义了可在管理网站中请求的所有URL
    path('users/',include('users.urls', namespace='users')), # 这行代码与任何以单词users打头的URL（如http://localhost:8000/users/login/） 都匹配
    path('', include('learning_logs.urls', namespace='learning_logs')), # 与书中不同 url这个方法变成了path，还有就是不需要r^等标识符。
   
]

'''
Django版本更新,书上的代码需做相应修改

书中源代码：
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('learning_logs.urls', namespace='learning_logs')),
]
应改为：
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls', namespace='learning_logs')),
]

'''