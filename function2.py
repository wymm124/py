#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 22:02
# @Author  : 日积跬步
# @File    : function2.py

"""函数的多个返回值"""


def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fun(lst))

"""
如果函数不需要返回值，return省略
如果函数只有一个返回值，直接返回类型
如果函数有多个返回值，则返回一个元组
"""