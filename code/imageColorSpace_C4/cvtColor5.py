# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 15:00 
  @File    : cvtColor5.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : HSV 实现艺术效果
"""

import cv2 as cv

img = cv.imread("../../data/lena.jpg")

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

h, s, v = cv.split(hsv)

v[:, :] = 255
# print(h)
# print(s)
print(v)
print(v.shape)

cv.imshow("bgr", img)
cv.imshow("hsv", hsv)

cv.waitKey()
cv.destroyAllWindows()
