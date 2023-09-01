# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.31 11:12 
  @File    : remap2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 重映射之复制 - cv.remap()
"""

import numpy as np
import cv2 as cv

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)

h, w = img.shape

mapx = np.zeros(img.shape, np.float32)
mapy = np.zeros(img.shape, np.float32)

for i in range(h):
    for j in range(w):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)

rst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
