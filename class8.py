#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 16:25
# @Author  : 日积跬步
# @File    : class8.py

"""特殊的-属性-方法"""


class Student(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ 方法被调用了, cls 的 id值 为: {0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象 id值 为: {}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__ 方法被调用了, self 的 id值 为: {0}'.format(id(self)))
        self.name = name
        self.age = age


print('object 这个类对象的 id值 为: {0}'.format(id(object)))
print('Student 这个类对象的 id值 为: {0}'.format(id(Student)))

stu1 = Student('张三', 20)
print('stu1 这个实例对象的 id值 为: {0}'.format(id(stu1)))

