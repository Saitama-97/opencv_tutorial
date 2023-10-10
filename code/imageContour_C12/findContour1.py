# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.10 09:28
  @File    : findContour1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 查找图像轮廓 - cv.findContour
"""

import cv2 as cv

img = cv.imread("../../data/contours.bmp")

cv.imshow("original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

o = cv.drawContours(binary, contours, -1, (0, 255, 0))

cv.imshow("result", o)

cv.waitKey()
cv.destroyAllWindows()
