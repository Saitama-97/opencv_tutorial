# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.10 14:56
  @File    : convexHull1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 轮廓的凸包 - cv.convexHull()
"""

import cv2 as cv

o = cv.imread("../../data/contours.bmp")

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

hull = cv.convexHull(contours[0])

print(hull)

print("*****")

hull2 = cv.convexHull(contours[0], returnPoints=False)

print(hull2)
