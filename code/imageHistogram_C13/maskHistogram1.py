# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 10:34
  @File    : maskHistogram1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 使用掩模构建直方图实例
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

o = cv.imread("../../data/lena.jpg")

print(o.shape)

mask = np.zeros([512, 512], np.uint8)
mask[200:400, 200:400] = 255

hist_b = cv.calcHist([o], [0], mask, [256], [0, 255])
hist_g = cv.calcHist([o], [1], mask, [256], [0, 255])
hist_r = cv.calcHist([o], [2], mask, [256], [0, 255])

plt.plot(hist_b)
plt.plot(hist_g)
plt.plot(hist_r)
plt.show()
