# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.12 09:45
  @File    : dilate2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像膨胀测试
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/dilation.bmp")

kernel = np.ones((9, 9), dtype=np.uint8)

rst = cv.dilate(img, kernel)

cv.imshow("img", img)
cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()
