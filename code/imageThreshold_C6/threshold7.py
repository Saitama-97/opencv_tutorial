# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.01 11:22 
  @File    : threshold7.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 阈值处理 - OTSU，自动寻找阈值
"""

import numpy as np
import cv2 as cv

img = np.zeros((5, 5), dtype=np.uint8)

img[0:6, 0:6] = 123
img[2:6, 2:6] = 126

print("img=\n", img)

t1, thd = cv.threshold(img, 127, 255, type=cv.THRESH_BINARY)

print("thd=\n", thd)

t2, otsu = cv.threshold(img, 0, 255, type=cv.THRESH_OTSU)

print("otsu=\n", otsu)
