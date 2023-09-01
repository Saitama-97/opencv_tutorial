# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 17:34 
  @File    : perspective1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 透视变换 - cv.warpPerspective()
  和仿射变换的不同点，仿射需要三个点，透视需要四个点
"""

import cv2 as cv
import numpy as np

img = cv.imread("../data/boat.bmp")

h, w = img.shape[:2]

# 变换前后四个点的坐标
p1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
p2 = np.float32([[50, 50], [h - 50, 50], [50, w - 50], [h - 50, w - 50]])

M = cv.getPerspectiveTransform(p1, p2)

dst = cv.warpPerspective(img, M, dsize=(w, h))

cv.imshow("img", img)
cv.imshow("dst", dst)

cv.waitKey()
cv.destroyAllWindows()
