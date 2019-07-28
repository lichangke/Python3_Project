from django.shortcuts import render

from .models import Topic   # 导入了与所需数据相关联的模型

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')  # 这里向函数render() 提供了两个实参： 原始请求对象以及一个可用于创建网页的模板。

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added') # 查询数据库——请求提供Topic 对象， 并按属性date_added 对它们进行排序
    context = {'topics': topics} # 一个将要发送给模板的上下文。 上下文是一个字典， 其中的键是我们将在模板中用来访问数据的名称， 而值是我们要发送给模板的数据。 
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)