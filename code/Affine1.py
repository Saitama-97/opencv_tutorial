# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 16:51 
  @File    : Affine1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 仿射变换 - cv.warpAffine()
  平移变换
"""

import cv2 as cv
import numpy as np

img = cv.imread("../data/boat.bmp")
h, w = img.shape[:2]
x, y = 100, 200
M = np.float32([[1, 0, x], [0, 1, y]])
dst = cv.warpAffine(img, M, dsize=(w, h))

cv.imshow("raw", img)
cv.imshow("move", dst)

cv.waitKey()
cv.destroyAllWindows()
