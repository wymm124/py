#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 21:35
# @Author  : 日积跬步
# @File    : class.py.py

"""类"""


class Student:
    # 类属性
    native_home = '河南'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def learn(self):
        print('这是实例方法：类里边定义的称为方法')

    @classmethod
    def cm(cls):
        print('这是类方法。。')

    @staticmethod
    def sm():
        print('这是静态方法。。')


def drink():
    print('这是函数：类外边定义的称为函数')


stu1 = Student('张三', 20)
print(id(stu1))
print(stu1.name)
print(stu1.age)
# 第一种方式调用实例方法
stu1.learn()

print('------------------')

# 第二种方式调用实例方法
Student.learn(stu1)
