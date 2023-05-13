#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 23:43
# @Author  : 日积跬步
# @File    : class9.py.py

"""变量的赋值操作-浅拷贝-深拷贝"""


class Cpu(object):
    pass


class Disk(object):
    pass


class Computer(object):
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


print('变量的赋值操作')
cpu1 = Cpu()
cpu2 = cpu1
print(id(cpu1))
print(id(cpu2))

cpu = Cpu()
disk = Disk()
computer = Computer(cpu, disk)

print('浅拷贝: py一般都是浅拷贝 拷贝时 对象包含的子对象内容不拷贝 因此 源对象与拷贝对象会引用同一个子对象')
import copy
computer2 = copy.copy(computer)
print('对比 computer实例')
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

print('深拷贝: 使用 copy模块 的 deepcopy函数 递归拷贝对象中包含的子对象 源对象和拷贝对象所有的子对象也不相同')
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
