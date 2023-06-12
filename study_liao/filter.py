#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 10:34
# @Author  : 日积跬步
# @File    : filter.py

# filter：接收一个函数、一个序列，把传入的函数依次作用于每个元素，根据返回值是 True、False 决定保留还是丢弃该元素

def func_not_empty(s):
    return s and s.strip()


def func_filter():
    lst = list(filter(func_not_empty, ['a', '', None, ' ']))
    print(lst)


# 埃氏筛法
def ai_shi_shai_fa(n):
    is_prime_lst = [True] * (n + 1)
    prime = []
    for i in range(2, n + 1):
        if is_prime_lst[i]:
            prime.append(i)
            for x in range(i * i, n + 1, i):
                is_prime_lst[x] = False
    return prime


# 返回回数：从左向右读、从右向左读都一样的数
def hui_shu(n):
    return str(n) == str(n)[::-1]


def func_filter2():
    lst = range(1, 200)
    hui_lst = list(filter(hui_shu, lst))
    print(hui_lst)


if __name__ == '__main__':
    # func_filter()
    # _odd_iter()
    # print(ai_shi_shai_fa(100))
    func_filter2()

