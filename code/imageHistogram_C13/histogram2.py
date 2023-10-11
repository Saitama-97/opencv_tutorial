# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 09:56
  @File    : histogram2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像直方图方法2 - cv.calHist() + plt.plot()
"""
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread("../../data/boat.bmp")

hist = cv.calcHist([img], [0], None, [16], [0, 255])

plt.plot(hist)
plt.show()

