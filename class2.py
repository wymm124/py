#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 21:35
# @Author  : 日积跬步
# @File    : class8.py.py

"""类属性 类方法 静态方法 使用"""


class Student:
    # 类属性：被该类的所有对象共享
    native_home = '河南'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def learn(self):
        print('这是实例方法：类里边定义的称为方法')

    @classmethod
    def cm(cls):
        print('这是类方法。。使用类名直接访问')

    @staticmethod
    def sm():
        print('这是静态方法。。使用类名直接访问')


print('类属性的使用----------------')
# 获取类属性
print(Student.native_home)
# 创建实例 & 获取类属性
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_home)
print(stu2.native_home)
print('修改类属性')
Student.native_home = '北京'
print(stu1.native_home)
print(stu2.native_home)
print('类方法的使用----------------')
Student.cm()
print('静态方法的使用----------------')
Student.sm()

