from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Topic, Entry
from .forms import TopicForm,EntryForm
from django.urls import reverse
# from django.core.urlresolvers import reverse
'''
https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers
Django 2.0 removes the django.core.urlresolvers module, which was moved to django.urls in version 1.10.
You should change any import to use django.urls instead, like this:
from django.urls import reverse
'''
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

# 函数new_topic() 需要处理两种情形： 刚进入new_topic 网页（在这种情况下， 它应显示一个空表单） ； 对提交的表单数据进行处理， 并将用户重定向到网页topics
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据： 创建一个新表单
        form = TopicForm()  # 如果请求方法不是POST， 请求就可能是GET， 因此我们需要返回一个空表单
    else:
        if form.is_valid(): # 必须先通过检查确定它们是有效的
            form.save() # 表单中的数据写入数据库
            # 函数reverse() 根据指定的URL模型确定URL， 这意味着Django将在页面被请求时生成URL。 
            # 调用HttpResponseRedirect() 将用户重定向到显示新增条目所属主题的页面
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
    '''
    创建Web应用程序时， 将用到的两种主要请求类型是GET请求和POST请求。 对于只是从服务器读取数据的页面， 使用GET请求； 在用户需要通过表单提交信息时， 通常使用POST
    请求。 处理所有表单时， 我们都将指定使用POST方法。 还有一些其他类型的请求， 但这个项目没有使用。
    函数new_topic() 将请求对象作为参数。 用户初次请求该网页时， 其浏览器将发送GET请求； 用户填写并提交表单时， 其浏览器将发送POST请求。 根据请求的类型， 我们可以
    确定用户请求的是空表单（GET请求） 还是要求对填写好的表单进行处理（POST请求） 。
    '''

def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid(): 
            # 调用save() 时， 传递了实参commit=False , 让Django创建一个新的条目对象， 并将其存储到new_entry 中， 但不将它保存到数据库中。
            new_entry = form.save(commit=False)
            new_entry.topic = topic # 将new_entry的属性topic 设置为在这个函数开头从数据库中获取的主题
            new_entry.save()    # 调用save() ， 且不指定任何实参。 这将把条目保存到数据库， 并将其与正确的主题相关联。
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)



def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求， 使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据， 对数据进行处理
        # 让Django根据既有条目对象创建一个表单实例， 并根据request.POST 中的相关数据对其进行修改
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)