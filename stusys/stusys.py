#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/29 23:28
# @Author  : 日积跬步
# @File    : stusys.py.py


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
    pass


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


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