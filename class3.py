#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 22:57
# @Author  : 日积跬步
# @File    : class3.py

"""动态绑定 属性-方法"""


class Student:
    native_home = '河南'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 10)
stu2 = Student('李四', 15)

print('动态绑定参数-----------------')
# 给 stu1实例 动态绑定属性
stu1.gender = '女'
print(stu1.name, stu1.age, stu1.gender)
stu1.eat()
# 如果没有给 stu2实例动态绑定 则获取 stu2实例的gender属性 会报错
print(stu2.name, stu2.age)
# print(stu2.gender)

print('动态绑定方法-----------------')


def dance():
    print('在跳舞。。定义在类之外, 称为函数')


stu1.show = dance()
stu1.show
