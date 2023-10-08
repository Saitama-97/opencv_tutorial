# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.08 10:39
  @File    : canny1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : Canny 边缘检测，阈值越小，能保留更多细节
"""

import cv2 as cv

img = cv.imread("../../data/lena.bmp")

r1 = cv.Canny(img, 128, 200)
r2 = cv.Canny(img, 50, 128)

cv.imshow("raw", img)
cv.imshow("r1", r1)
cv.imshow("r2", r2)

cv.waitKey()
cv.destroyAllWindows()
