# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.02 10:58 
  @File    : Blur6.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像平滑处理 - 2D卷积 - cv.filter2D(img, ddepth, kernel, anchor, delta, borderType)
            kernel : 卷积核
            delta : 修正值，可选，如果有，则会在基础滤波的结果上加上该值作为最终结果
"""

import cv2 as cv
import numpy as np

img = cv.imread("../data/lena.bmp")

kernel = np.ones((9, 9), np.float32) / 81

dst = cv.filter2D(img, ddepth=-1, kernel=kernel)

cv.imshow("img", img)
cv.imshow("dst", dst)

cv.waitKey()
cv.destroyAllWindows()
