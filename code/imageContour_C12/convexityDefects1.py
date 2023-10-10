# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.10 15:45
  @File    : convexityDefects1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 凸缺陷 - 凸包与轮廓之间的部分，cv.convexityDefects()
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/hand.bmp")

cv.imshow("original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

hull = cv.convexHull(cnt, returnPoints=False)
defects = cv.convexityDefects(cnt, hull)

print(defects)
