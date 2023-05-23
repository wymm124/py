#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 23:21
# @Author  : 日积跬步
# @File    : clearImage.py

import cv2


def get_water():
    # 黑底白字
    src = cv2.imread('xiao.png')  # 默认的彩色图(IMREAD_COLOR)方式读入原始图像
    print("有水印的图片<img width=300 src='xiao.png' />")
    # black.jpg
    mask = cv2.imread('xiaoBack.png', cv2.IMREAD_GRAYSCALE)  # 灰度图(IMREAD_GRAYSCALE)方式读入水印蒙版图像
    # 参数：目标修复图像; 蒙版图（定位修复区域）; 选取邻域半径; 修复算法(包括INPAINT_TELEA/INPAINT_NS， 前者算法效果较好)
    dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_NS)
    print("水印logo底色图片<img width=300 src='xiaoBack.png' />")

    cv2.imwrite('result234.png', dst)
    print("去除水印后的照片<img width=300 src='result234.png' />")


get_water()
