# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.10 10:13
  @File    : findContour2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像轮廓实例
"""

import cv2 as cv
import numpy as np

o = cv.imread("../../data/loc3.jpg")

cv.imshow("original", o)

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

mask = np.zeros(o.shape, np.uint8)
mask = cv.drawContours(mask, contours, -1, (255, 255, 255), -1)
cv.imshow("mask", mask)
loc = cv.bitwise_and(o, mask)
cv.imshow("location", loc)
cv.waitKey()
cv.destroyAllWindows()
