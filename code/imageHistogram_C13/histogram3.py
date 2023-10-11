# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 10:20
  @File    : histogram3.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像直方图实例
"""

import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread("../../data/lena.jpg")

hist_b = cv.calcHist(o, [0], None, [256], [0, 255])
hist_g = cv.calcHist(o, [1], None, [256], [0, 255])
hist_r = cv.calcHist(o, [2], None, [256], [0, 255])

plt.plot(hist_b, 'b')
plt.plot(hist_g, 'g')
plt.plot(hist_r, 'r')

plt.show()
