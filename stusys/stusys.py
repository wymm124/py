#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/29 23:28
# @Author  : 日积跬步
# @File    : stusys.py.py

import os

file_name = 'students.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择'))
        menu_list = [0, 1, 2, 3, 4, 5, 6, 7]
        if choice in menu_list:
            if choice == 0:
                ans = input('确认要退出吗y/n')
                if ans == 'y' or ans == 'Y':
                    print('谢谢使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            print('请重新输入')


def insert():
    # 列表
    student_list = []
    while True:
        stu_id = input('请输入id：')
        if not stu_id:
            break
        stu_name = input('请输入名字')
        if not stu_name:
            break
        try:
            english = int(input('请输入english成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('非法成绩')
            continue
        # 将学生信息放入字典中
        stu = {'id': stu_id, 'name': stu_name, 'english': english, 'python': python, 'java': java}
        # 将学生放入集合中
        student_list.append(stu)
        continue_ans = input('是否继续y/n')
        if 'y' == continue_ans:
            continue
        else:
            break

    # 调用 save函数 保存到文件
    save(student_list)
    print('录入结束')


def save(lst):
    try:
        stu_txt = open(file_name, 'a', encoding='utf-8')
    except:
        stu_txt = open(file_name, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    pass


def delete():
    while True:
        del_stu_id = input('请输入要删除学生的id：')
        if del_stu_id != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as r_file:
                    stu_old = r_file.readlines()
            else:
                stu_old = []
            flag = False
            if stu_old:
                with open(file_name, 'w', encoding='utf-8') as w_file:
                    d = {}
                    for item in stu_old:
                        d = dict(eval(item))
                        if d['id'] != del_stu_id:
                            w_file.write(item)
                        else:
                            flag = True
                    if flag:
                        print('已删除指定学生')
                    else:
                        print(f'没有找到id为{del_stu_id}的学生')
            else:
                print('没有学生信息')
                break
            # 删除完毕后重新展示学生信息
        show()
        answer = input('是否继续删除y/n')
        if 'y' == answer:
            continue
        else:
            break


def modify():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as r_file:
            stu_old = r_file.readlines()
    else:
        print('不存在学生信息')
        return
    modify_stu = input('请输入要修改学生的id：')
    flag = True
    with open(file_name, 'w', encoding='utf-8') as w_file:
        for item in stu_old:
            d = dict(eval(item))
            if d['id'] == modify_stu:
                flag = False
                print('找到了，可以进行修改')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['java'] = input('请输入java成绩：')
                        d['python'] = input('请输入python成绩：')
                    except:
                        print('输入有误，重新输入')
                    else:
                        break
                w_file.write(str(d) + '\n')
                print('修改成功')
                break
            else:
                w_file.write(str(d) + '\n')
        if flag:
            print('没有找到学生')
    answer = input('是否继续修改y/n')
    if 'y' == answer:
        modify()
    else:
        return


def sort():
    pass


def total():
    pass


def show():
    print('show msg')


def menu():
    print("=======学生信息管理系统=======")
    print('-----------功能菜单-----------')
    print('\t\t1.录入学生信息')
    print('\t\t2.查找学生信息')
    print('\t\t3.删除学生信息')
    print('\t\t4.修改学生信息')
    print('\t\t5.排序')
    print('\t\t6.统计学生总人数')
    print('\t\t7.显示所有学生信息')
    print('\t\t0.退出')


if __name__ == '__main__':
    main()