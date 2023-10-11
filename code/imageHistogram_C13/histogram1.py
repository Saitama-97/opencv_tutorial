# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 09:27
  @File    : histogram1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像直方图方法1 - matplotlib.pyplot.hist(X, BINS)
"""

import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread("../../data/boat.bmp")

cv.imshow("origin", o)

data = o.ravel()

plt.hist(data, 16)
plt.show()

cv.waitKey()
cv.destroyAllWindows()