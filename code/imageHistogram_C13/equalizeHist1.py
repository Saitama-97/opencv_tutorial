# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 10:58
  @File    : equalizeHist1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 直方图均衡化 - cv.equalizeHist()
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../../data/equ.bmp", 0)

equ = cv.equalizeHist(img)

cv.imshow("origin", img)
cv.imshow("equalized", equ)

plt.hist(img.ravel(), 256, color="r")
plt.hist(equ.ravel(), 256, color="g")

plt.show()

cv.waitKey()
cv.destroyAllWindows()
