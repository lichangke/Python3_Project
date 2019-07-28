# -*- coding: utf-8 -*-
# @Author   : leacoder
# @Time     : 2019/7/27 12:38
# @File     : student_system.py
# @Software : PyCharm
# @Contact  : https://www.jianshu.com/u/3e95c7555dc7
# @Contact  : https://www.zhihu.com/people/lichangke/activities
# @Desc     : 

import re  # 导入正则表达式模块
import os  # 导入操作系统模块

filename = 'students.txt'  # 定义保存学生信息的文件名


def menu():
    # 菜单
    print("""
    ╔———————学生信息管理系统————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1 录入学生信息                             │
    │   2 查找学生信息                             │
    │   3 删除学生信息                             │
    │   4 修改学生信息                             │
    │   5 排序                                     │
    │   6 统计学生总人数                           │
    │   7 显示所有学生信息                         │
    │   0 退出系统                                 │
    │  ==========================================  │
    │  说明：通过数字选择菜单                      │
    ╚———————————————————————╝
    """)


"""主函数"""


def main():
    flag_ctrl = True  # 循环变量
    while flag_ctrl:
        menu()  # 显示主菜单
        option_str = input('请选择：')
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if 0 == option_int:  # 退出系统
                print('你已退出学生信息管理系统！')
                flag_ctrl = False
            elif 1 == option_int:  # 录入学生成绩信息
                insert()
            elif 2 == option_int:  # 查找学生成绩信息
                search()
            elif 3 == option_int:  # 删除学生成绩信息
                delete()
            elif 4 == option_int:  # 修改学生成绩信息
                modify()
            elif 5 == option_int:  # 排序
                sort()
            elif 6 == option_int:  # 统计学生总数
                total()
            elif 7 == option_int:  # 显示所有学生信息
                show()
        else:
            print('输入错误\r\n')


"""1 录入学生信息"""


def insert():
    """
    1、提示输入： 学生编号、学生姓名、学生成绩(英语、Python、C)  校验输入是否符合要求
    2、输入正确后，提示是否继续添加 Y N， Y：继续添加 N：保存信息后退出
    """
    student_list = []  # 里面存储单个学生的信息（字典类型）的列表
    mark_flag = True
    while mark_flag:
        id = input('请输入ID（如 1001）：')
        if not id:  # ID为空，跳出循环
            break
        name = input('请输入名字：')
        if not name:  # 名字为空，跳出循环
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            c = int(input('请输入C语言成绩：'))
        except:
            print('输入无效，不是整型数值．．．．重新录入信息')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'c': c}  # 将输入的学生信息保存到字典
        student_list.append(student)  # 将学生字典添加到列表中
        continue_mark = input('是否继续添加？（y/n）:')
        if 'y' == continue_mark or 'Y' == continue_mark:
            mark_flag = True
        else:
            mark_flag = False
        save(student_list)  # 保存信息到txt文档
        print('学生信息录入完毕！！！')


def save(student_list):
    """
    将学生信息保存到文件
    需要注意的是编码的不同 UTF-8 与 GBK
    :param student_list: 学生信息列表，元素为字典
    """
    # Python判断文件是否存在的三种方法 ： https://www.cnblogs.com/jhao/p/7243043.html
    try:
        students_txt = open(filename, 'a')  # 以追加模式打开
    except FileNotFoundError:
        students_txt = open(filename, 'w')  # 文件不存在，创建文件并打开
    for student in student_list:
        students_txt.write(str(student) + '\n')  # 按行存储，添加换行符
    students_txt.close()  # 关闭文件


"""2 查找学生成绩信息"""


def search():
    """
    1、判断txt文件是否存在，不存在：提示，存在 ：按提示选择查找类型
    2、读取txt文件内容并存入list中，按查找类型查找学生信息
    """
    mark_flag = True
    student_query = []  # 保存查询结果的学生列表
    while mark_flag:
        student_id = name = ''
        if os.path.exists(filename):
            mode = input('按ID查输入1；按姓名查输入2：')
            if mode == '1':
                student_id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入！')
                continue  # 重新查询
            with open(filename, 'r') as file:  # 打开文件
                student_list = file.readlines()  # 读取全部内容
                for student_info in student_list:
                    student_info_dict = dict(eval(student_info))  # 字符串转字典
                    if student_id is not '':  # 判断是否按ID查
                        if student_info_dict['id'] == student_id:
                            student_query.append(student_info_dict)  # 将找到的学生信息保存到列表中
                    elif name is not '':  # 判断是否按姓名查
                        if student_info_dict['name'] == name:
                            student_query.append(student_info_dict)  # 将找到的学生信息保存到列表中
                show_student(student_query)  # 显示查询结果
                student_query.clear()  # 清空列表
                continue_mark = input('是否继续查询？（y/n）:')
                if 'y' == continue_mark or 'Y' == continue_mark:
                    mark_flag = True
                else:
                    mark_flag = False
        else:
            print('无学生信息...')
            return  # 直接退出循环


"""3 删除学生成绩信息"""


def delete():
    """
    1、提示输入删除的学生ID，判断是否为空
    2、判断文件是否存在，存在：按行读取并存入list中
    3、遍历list跳过输入ID的学生信息将是其他人的信息重新写入txt
    """
    mark_flag = True
    while mark_flag:
        student_id = input('请输入要删除的学生ID：')
        if student_id is not '':  # 判断是否为空,不为空处理，为空继续
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r') as rfile:  # 打开文件,  上下文管理器 https://www.jianshu.com/p/60864aef596b
                    students_old_list = rfile.readlines()  # 读取全部内容 （内容可能为空）
            else:
                students_old_list = []
            ifdel = False  # 标记是否删除
            if students_old_list:  # 存在学生信息，进行处理
                with open(filename, 'w') as wfile:  # 以写方式打开文件
                    student_info_dict = {}  # 存入时我们知道是按字典形式
                    for student_info in students_old_list:
                        """eval()函数
                        https://stackoverflow.com/questions/9383740/what-does-pythons-eval-do
                        https://docs.python.org/zh-cn/3/library/functions.html#eval
                        eval(expression, globals=None, locals=None)
                        expression 参数一个字符串会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值
                        student_info，形如 ''{'id': '1001', 'name': '张三', 'english': 88, 'python': 90, 'c': 97}'' 这种字符串
                        result = eval(student_info) ，result 类型 <class 'dict'>
                        dict(eval(student_info)) 可以起一个提示作用
                        """
                        student_info_dict = dict(eval(student_info))  # 字符串转字典
                        if student_info_dict['id'] != student_id:  # 不是删除的学生信息
                            wfile.write(str(student_info_dict) + '\n')  # 将一条学生信息写入文件
                        else:
                            ifdel = True  # 标记已经删除
                    if ifdel:
                        print('ID为 %s 的学生信息已经被删除...'.format(student_id))
                    else:
                        print('没有找到ID为 %s 的学生信息...'.format(student_id))

            else:  # 不存在学生信息
                print('无学生信息...')
                return  # 直接退出循环
            show()  # 显示全部学生信息
            continue_mark = input('是否继续删除？（y/n）:')
            if 'y' == continue_mark or 'Y' == continue_mark:
                mark_flag = True  # 继续删除
            else:
                mark_flag = False  # 退出删除学生信息功能
        else:
            continue


"""4 修改学生成绩信息"""


def modify():
    """流程类似def delete():
    1、show()  # 显示全部学生信息
    2、提示输入修改的学生ID，判断txt是否存在，存在则读取全部内容并保存到list
    3、遍历list，更具提示修改输入ID的学生信息，并将修改后的学生信息以及没修改的信息保存到txt
    """
    mark_flag = True
    while mark_flag:
        show()  # 显示全部学生信息
        student_id = input('请输入要修改的学生ID：')
        if os.path.exists(filename):  # 判断文件是否存在
            with open(filename, 'r') as rfile:  # 打开文件
                student_old_list = rfile.readlines()  # 读取全部内容
        else:
            print('读取文件｛｝失败'.format(filename))
            break  # 直接退出循环
        flag_find = False
        with open(filename, 'w') as wfile:  # 以写模式打开文件
            for student_info in student_old_list:
                tudent_info_dict = dict(eval(student_info))  # 字符串转字典
                if tudent_info_dict['id'] == student_id:  # 是否为要修改的学生
                    print('找到了这名学生，可以修改他的信息！')
                    flag_find = True
                    flag = True
                    while flag:  # 输入要修改的信息
                        try:
                            tudent_info_dict['name'] = input('请输入姓名：')
                            tudent_info_dict['english'] = int(input('请输入英语成绩：'))
                            tudent_info_dict['python'] = int(input('请输入Python成绩：'))
                            tudent_info_dict['c'] = int(input('请输入C语言成绩：'))
                        except:
                            print('您的输入有误，请重新输入。')
                        else:
                            flag = False  # 跳出循环
                    student_info = str(tudent_info_dict)  # 将字典转换为字符串
                    wfile.write(student_info + '\n')  # 将修改的信息写入到文件
                    print('修改成功！')
                else:
                    wfile.write(student_info)  # 将未修改的信息写入到文件
        if not flag_find:
            print('未找到id为｛｝的学生'.format(student_id))
        continue_mark = input('是否继续修改其他学生信息？（y/n）：')
        if 'y' == continue_mark or 'Y' == continue_mark:
            mark_flag = True  # 继续修改操作
        else:
            mark_flag = False  # 退出修改操作


"""5 排序"""


def sort():
    """
    1、判断文件是否存在，不存在提示
    2、存在，更具输入选择排序方式和按什么排序
    :return:
    """
    show()  # 显示全部学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as file:  # 打开文件
            student_old = file.readlines()  # 读取全部内容
            student_new = []
        for student_info in student_old:
            student_info_dict = dict(eval(student_info))  # 字符串转字典
            student_new.append(student_info_dict)  # 将转换后的字典添加到列表中
    else:
        print('暂未保存数据信息...')
        return
    asc_desc = input("请选择（0升序；1降序）：")
    if asc_desc == "0":  # 按升序排序
        asc_desc_flag = False  # 标记变量，为False表示升序排序
    elif asc_desc == "1":  # 按降序排序
        asc_desc_flag = True  # 标记变量，为True表示降序排序
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式（0按总成绩排序，1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；4按ID排序）：")
    if mode == "1":  # 按英语成绩排序
        student_new.sort(key=lambda x: x["english"], reverse=asc_desc_flag)
    elif mode == "2":  # 按Python成绩排序
        student_new.sort(key=lambda x: x["python"], reverse=asc_desc_flag)
    elif mode == "3":  # 按C语言成绩排序
        student_new.sort(key=lambda x: x["c"], reverse=asc_desc_flag)
    elif mode == "0":  # 按总成绩排序
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=asc_desc_flag)
    elif mode == "4":  # 按C语言成绩排序
        student_new.sort(key=lambda x: x["id"], reverse=asc_desc_flag)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)  # 显示排序结果


""" 6 统计学生总数"""


def total():
    """
    1、判断文件是否存在，不存在提示
    2、已存在，读取txt信息保存在list中，并统计学生人数
    """
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
            if student_old:
                print('一共有 {} 名学生！'.format(len(student_old)))
            else:
                print('还没有录入学生信息！')
    else:
        print('暂未保存数据信息...')


""" 7 显示所有学生信息 """


def show():
    """
    1、判断文件是否存在，不存在提示
    2、已存在，读取txt信息保存在list中
    3、遍历list格式化显示学生信息
    """
    student_new = []
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old_list = rfile.readlines()  # 读取全部内容 list元素是字符串
        for student_old_info in student_old_list:
            student_new.append(eval(student_old_info))  # 将找到的学生信息保存到列表中 这里元素变为字典
        if student_new:
            show_student(student_new)
        else:
            print('(=。=) 无数据信息 (=。=) \n')

    else:
        print('暂未保存数据信息...')


# 将保存在列表中的学生信息显示出来
def show_student(student_list):
    if student_list:  # 不为空 格式化显示
        format_title = '{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}'
        print(format_title.format('ID', '名字', '英语成绩', 'Python成绩', 'C语言成绩', '总成绩'))
        format_data = '{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
        for student_info in student_list:
            english, python, c = student_info.get('english'), student_info.get('python'), student_info.get('c')
            total_score = english + python + c
            print(format_data.format(student_info.get('id').center(6), student_info.get('name').center(12),
                                     str(english).center(12), str(python).center(12), str(c).center(12),
                                     str(total_score).center(12)))
    else:
        print('(=。=) 无数据信息 (=。=) \n')


if __name__ == '__main__':
    main()
