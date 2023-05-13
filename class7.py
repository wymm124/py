#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 15:27
# @Author  : 日积跬步
# @File    : class7.py

"""特殊的-属性-方法"""

print('整数类型的特殊方法 __add__')
a = 10
b = 20
c = a + b
print(c)
d = a.__add__(b)
print(d)

print('字符串类型的特殊方法 __add__')
aa = 'a'
bb = 'b'
print(aa + bb)
print(aa.__add__(bb))

print('实例类型的特殊方法 __add__')


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三', 10)
stu2 = Student('李四', 20)

print(stu1.__add__(stu2))


print('列表类型的特殊方法 __len__')
# 获取列表的len
lst = ['a', 'b', 'c', 'd', 'e']
print(len(lst))

print('实例类型的特殊方法 __len__')
# 获取对象的len
stu3 = Student('rose', 18)
print(len(stu3))

