#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 23:28
# @Author  : 日积跬步
# @File    : module2.py

"""导入自定义模块 module-calc 中的所有内容"""

import calc

print('调用自定义模块中的函数')
res = calc.add(1, 2)
print(res)
