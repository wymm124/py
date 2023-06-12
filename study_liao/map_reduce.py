#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 0:19
# @Author  : 日积跬步
# @File    : map_reduce.py

from functools import reduce

"""
map：将传入的函数依次作用于序列的每一个元素上
reduce：把一个函数作用在一个序列 [1, 2, 3, 4] 上，函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累计计算
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


print('开始reduce')


def func11(m, n):
    return m + n


def func_reduce1():
    res = reduce(func11, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(res)


def func12(m, n):
    return m * 10 + n


def func_char2num(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]


def func_reduce2():
    lst = list(map(func_char2num, '123456'))
    res = reduce(func12, lst)
    print(res)


if __name__ == '__main__':
    # func_map()
    # func_map2()
    # func_reduce1()
    func_reduce2()

