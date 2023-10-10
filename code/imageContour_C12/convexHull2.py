# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.10 15:08
  @File    : convexHull2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 凸包实例 - cv.convexHull()
"""

import cv2 as cv
import numpy as np

o = cv.imread("../../data/hand.bmp")

cv.imshow("origin", o)

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

hull = cv.convexHull(contours[0])

cv.polylines(o, [hull], True, 255, 2)

cv.imshow("result", o)

cv.waitKey()
cv.destroyAllWindows()
