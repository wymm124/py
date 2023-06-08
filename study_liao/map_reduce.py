#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 0:19
# @Author  : 日积跬步
# @File    : map_reduce.py

"""
map：将传入的函数依次作用于序列的每一个元素上
"""


def func(n):
    return n * n


def func_map():
    lst = list(map(func, [1, 2, 3]))
    print(lst)


def func2(x, y):
    return x + y


def func_map2():
    lst = list(map(func2, [1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))
    print(lst)


if __name__ == '__main__':
    # func_map()
    func_map2()

