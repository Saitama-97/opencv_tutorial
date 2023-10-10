# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.10 10:25
  @File    : moments1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 矩特征 - cv.moments()
            零阶矩 m00 - 轮廓的面积
            也可以用 cv.contourArea() 获取轮廓的面积
"""

import cv2 as cv
import numpy as np

o = cv.imread("../../data/contours.bmp")

cv.imshow("original", o)

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

n = len(contours)

contoursImg = []

for i in range(n):
    temp = np.zeros(binary.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv.drawContours(contoursImg[i], contours, i, 255, 3)
    cv.imshow("contours[" + str(i) + "]", contoursImg[i])

print("观察每个轮廓的矩:")
for i in range(n):
    print("轮廓" + str(i) + "的矩:\n", cv.moments(contours[i]))

print("观察每个轮廓的面积:")
for i in range(n):
    print("轮廓" + str(i) + "的面积:\n", cv.moments(contours[i])["m00"])
    print("轮廓" + str(i) + "的面积:\n", cv.contourArea(contours[i]))
    print()

cv.waitKey()
cv.destroyAllWindows()
