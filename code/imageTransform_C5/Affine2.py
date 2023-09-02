# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 17:03 
  @File    : Affine2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 仿射变化 - cv.warpAffine()
  旋转
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/boat.bmp")
h, w = img.shape[:2]

M = cv.getRotationMatrix2D((w / 2, h / 2), 45, 0.5)
dst = cv.warpAffine(img, M, dsize=(w, h))

cv.imshow("raw", img)
cv.imshow("move", dst)

cv.waitKey()
cv.destroyAllWindows()
