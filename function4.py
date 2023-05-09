#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 22:50
# @Author  : 日积跬步
# @File    : function4.py

"""
个数可变的位置参数
使用 * 定义一个可变参数
返回结果为一个元组
"""


def fun(*args):
    print(args)
    print(args[0])


fun(1)
fun(10, 20)
fun(100, 200, 300)

