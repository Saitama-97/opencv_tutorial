# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.02 10:39 
  @File    : Blur4.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像平滑处理 - 中值滤波 - cv.medianBlur(img, ksize)
"""

import cv2 as cv

img = cv.imread("../../data/lenaNoise.png")

dst = cv.medianBlur(img, ksize=5)

cv.imshow("img", img)
cv.imshow("MedianBlur", dst)

cv.waitKey()
cv.destroyAllWindows()
