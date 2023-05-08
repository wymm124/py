#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/7 9:11
# @Author  : 日积跬步
# @File    : function.py

def calc(a, b):
    c = a + b
    return c


result = calc(1, 9)
print(result)

print('=================')


def myfun(arg1, arg2):
    print(arg1)
    print(arg2)

    arg1 = 100
    arg2.append(200)
    print(arg1)
    print(arg2)


a = 10
# 列表
b = [1, 2, 3, 4, 5]
print('调用函数前a: ', a)
print('调用函数前b: ', b)
print('调用函数中')
myfun(a, b)
print('调用函数中')
print('调用函数后a: ', a)
print('调用函数后b: ', b)
