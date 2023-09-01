# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.31 10:40 
  @File    : remap1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 重映射 - cv.remap()
  mapx - 指定列
  mapy - 指定行
"""

import cv2 as cv
import numpy as np

# 灰度图
img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
# height, width
h, w = img.shape
mapx = np.ones(img.shape, np.float32) * 3
mapy = np.ones(img.shape, np.float32) * 0
rst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
print()
