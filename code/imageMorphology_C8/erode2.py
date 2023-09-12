# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.12 09:31
  @File    : erode2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像腐蚀测试
"""

import numpy as np
import cv2 as cv

img = cv.imread("../../data/erode.bmp")

kernel = np.ones((9, 9), dtype=np.uint8)

rst = cv.erode(img, kernel)

cv.imshow("raw", img)
cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()
