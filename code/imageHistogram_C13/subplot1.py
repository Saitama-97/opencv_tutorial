# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 11:29
  @File    : subplot1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : matplotlib.pyplot.subplot
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../../data/equ.bmp", 0)

equ = cv.equalizeHist(img)

plt.figure("subplot实例")

plt.subplot(121)
plt.hist(img.ravel(), 256)

plt.subplot(122)
plt.hist(equ.ravel(), 256)

plt.show()
