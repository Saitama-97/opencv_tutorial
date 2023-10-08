# _*_ coding: utf-8 _*_

"""
  @Time    : 2023/10/2 14:20 
  @File    : scharr1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像梯度计算 - Scharr算子
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/scharr.bmp")

scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)
scharry = cv.Scharr(img, cv.CV_64F, 0, 1)

scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.convertScaleAbs(scharry)

scarrxy = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

cv.imshow("origin", img)
cv.imshow("scarrxy", scarrxy)

cv.waitKey()
cv.destroyAllWindows()
