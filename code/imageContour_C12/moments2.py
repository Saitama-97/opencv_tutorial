# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.10 14:21
  @File    : moments2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 轮廓的长度 - cv.arcLength
"""

import cv2 as cv
import numpy as np

o = cv.imread("../../data/contours.bmp")

cv.imshow("origin", o)

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

n = len(contours)
cntLen = []

for i in range(n):
    cntLen.append(cv.arcLength(contours[i], True))
    print("第" + str(i) + "个轮廓的长度为:" + str(cntLen[i]))

cntLenSum = np.sum(cntLen)
cntLenAvr = cntLenSum / n

print("轮廓总长度为:" + str(cntLenSum))
print("轮廓平均长度为:" + str(cntLenAvr))

contoursImg = []
# 显示超过平均长度的轮廓
for i in range(n):
    temp = np.zeros(o.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv.drawContours(contoursImg[i], contours, i, 255, 3)
    if cv.arcLength(contours[i], True) > cntLenAvr:
        cv.imshow("contours[" + str(i) + "]", contoursImg[i])

cv.waitKey()
cv.destroyAllWindows()
