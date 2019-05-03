from django.shortcuts import render

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')  # 这里向函数render() 提供了两个实参： 原始请求对象以及一个可用于创建网页的模板。