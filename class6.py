#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 0:42
# @Author  : 日积跬步
# @File    : class6.py

"""特殊的-属性-方法"""


class A(object):
    pass


class B(object):
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass


c = C('张三', 18)
# 实例对象的属性字典
print(c.__dict__)
# 类对象的属性字典
print(C.__dict__)
# 对象所属的类
print(c.__class__)
# 类对象的父类
print(C.__bases__)
print(C.__base__)
# 类的层次结构
print(C.__mro__)
# 子类的列表
print(A.__subclasses__())
