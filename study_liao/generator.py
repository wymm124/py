#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 21:57
# @Author  : 日积跬步
# @File    : generator.py

# 1、生成器：保存的是算法，当获取的时候才计算出来下一个值，不用创建完整的list，节省空间
def prac_generator():
    gene = (i for i in range(5))
    print('生成器类型：{}'.format(type(gene)))
    print(gene)
    for i in gene:
        print(i)


# 2、斐波那契数列
def fib(n):
    i = 0
    fib_num1 = 1
    fib_num2 = 0
    while i < n:
        print(fib_num1)
        fib_num1, fib_num2 = fib_num1 + fib_num2, fib_num1
        i += 1
    print('done')


# 3、函数中存在yield，则是生成器函数，执行逻辑：遇到yield则中断，下次继续执行
def func_generator():
    print('1')
    yield
    print('2')
    yield
    print('3')


# 4、杨辉三角
def yh_triangle():
    a = [1]
    while True:
        # yield a
        print(a)
        a = [1] + [a[i] + a[i + 1] for i in range(len(a)) if len(a) >= 2 and i < len(a) - 1] + [1]
        if len(a) == 9:
            break


if __name__ == '__main__':
    # prac_generator()
    # fib(8)
    yh_triangle()
