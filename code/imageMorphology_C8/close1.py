# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.12 10:07
  @File    : close1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像形态学运算 - 闭运算 - 先膨胀再腐蚀
"""

import cv2 as cv
import numpy as np

img1 = cv.imread("../../data/closing.bmp")
img2 = cv.imread("../../data/closing2.bmp")

k = np.ones((10, 10), np.uint8)

r1 = cv.morphologyEx(img1, op=cv.MORPH_CLOSE, kernel=k)
r2 = cv.morphologyEx(img2, op=cv.MORPH_CLOSE, kernel=k)

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("rst1", r1)
cv.imshow("rst2", r2)

cv.waitKey()
cv.destroyAllWindows()
