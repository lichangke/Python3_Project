from django import forms
from .models import Topic,Entry

# 让用户输入并提交信息的页面都是表单， 那怕它看起来不像表单。
# 创建表单的最简单方式是使用ModelForm， 它根据我们在第18章定义的模型中的信息自动创建表单。
class TopicForm(forms.ModelForm): # 定义了一个名为TopicForm 的类， 它继承了forms.ModelForm 。
    class Meta:
        model = Topic # 根据模型Topic 创建一个表单
        fields = ['text'] # 该表单只包含字段text 
        labels = {'text': ''} # 让Django不要为字段text 生成标签。


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        '''
        定义了属性widgets 。 小部件 （widget） 是一个HTML表单元素， 如单行文本框、 多行文本区域或下拉列表。 通过设置属性widgets ， 可覆盖Django选择的默认小
        部件。 通过让Django使用forms.Textarea ， 我们定制了字段'text' 的输入小部件， 将文本区域的宽度设置为80列， 而不是默认的40列。 这给用户提供了足够的空间， 可以
        编写有意义的条目。
        '''