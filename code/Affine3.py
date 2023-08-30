# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 17:17 
  @File    : Affine3.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 更复杂的仿射变换 - 通过 cv.getAffineTransform() 获取矩阵 M
"""

import cv2 as cv
import numpy as np

img = cv.imread("../data/lena.bmp")

h, w, c = img.shape

# 左上、右上、左下 变换前后 坐标
# [0,0] [w,0] [0,h]
p1 = np.float32([[0, 0], [w - 1, 0], [0, h - 1]])
p2 = np.float32([[0, h * 0.33], [w * 0.85, h * 0.25], [w * 0.15, h * 0.7]])

# 根据变换前后坐标计算出变换矩阵
M = cv.getAffineTransform(p1, p2)

dst = cv.warpAffine(img, M, dsize=(w, h))

cv.imshow("raw", img)
cv.imshow("result", dst)

cv.waitKey()
cv.destroyAllWindows()
