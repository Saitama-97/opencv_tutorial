# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 10:29
  @File    : mask1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 构建掩模（mask）实例
"""

import cv2 as cv
import numpy as np

mask = np.zeros([600, 600], dtype=np.uint8)

mask[200:400, 200:400] = 255

cv.imshow("mask", mask)

cv.waitKey()
cv.destroyAllWindows()
