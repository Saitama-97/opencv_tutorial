# _*_ coding: utf-8 _*_

"""
  @Time    : 2023/9/30 10:33 
  @File    : sobel1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像梯度计算 - Sobel算子
"""

import numpy as np
import cv2 as cv

img = cv.imread("../../data/sobel4.bmp")

Sobelx = cv.Sobel(img, -1, 1, 0)
Sobelx_64F = cv.convertScaleAbs(cv.Sobel(img, cv.CV_64F, 1, 0))

Sobely = cv.Sobel(img, -1, 0, 1)
Sobely_64F = cv.convertScaleAbs(cv.Sobel(img, cv.CV_64F, 0, 1))

Sobelxy_64F = cv.addWeighted(Sobelx_64F, 0.5, Sobely_64F, 0.5, 0)

cv.imshow("raw", img)
cv.imshow("Sobelx", Sobelx)
cv.imshow("Sobelx_64F", Sobelx_64F)
cv.imshow("Sobely", Sobely)
cv.imshow("Sobely_64F", Sobely_64F)
cv.imshow("Sobelxy_64F", Sobelxy_64F)

cv.waitKey()
cv.destroyAllWindows()
