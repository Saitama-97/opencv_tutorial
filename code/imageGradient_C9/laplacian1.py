# _*_ coding: utf-8 _*_

"""
  @Time    : 2023/10/2 17:02 
  @File    : laplacian.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像梯度计算 - 拉普拉斯算子
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/laplacian.bmp")
rst = cv.Laplacian(img, cv.CV_64F)
rst = cv.convertScaleAbs(rst)

cv.imshow("raw", img)
cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()
