#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 22:54
# @Author  : 日积跬步
# @File    : function5.py

"""
个数可变的关键字参数
使用 ** 定义个数可变的关键字参数
返回结果为一个字典
"""


def fun(**kwargs):
    print(kwargs)


d = {'a': '1', 'b': '2'}
# fun(a=1, b=2, c=3)
fun(**d)


def fun2(*args, **kwargs):
    print(args)
    print(kwargs)


# 以下代码编译错误, 函数中存在 位置参数、关键字参数, 位置参数必须放在关键字参数之前
"""
def fun2(**kwargs, *args):
    print(kwargs)
    print(args)
"""
