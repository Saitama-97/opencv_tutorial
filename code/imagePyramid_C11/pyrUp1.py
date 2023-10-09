# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.09 10:27
  @File    : pyrUp1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像金字塔 - 上采样，图像的宽和高均变成 2倍，整体变成 4倍
"""

import cv2 as cv

img = cv.imread("../../data/lena.bmp")

r1 = cv.pyrUp(img)
r2 = cv.pyrUp(r1)
r3 = cv.pyrUp(r2)

print("img-shape", img.shape)
print("r1-shape", r1.shape)
print("r2-shape", r2.shape)
print("r3-shape", r3.shape)

cv.imshow("img", img)
cv.imshow("r1", r1)
cv.imshow("r2", r2)
cv.imshow("r3", r3)

cv.waitKey()
cv.destroyAllWindows()
