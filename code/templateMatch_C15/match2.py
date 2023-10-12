# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.12 09:24
  @File    : match2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 单模板匹配实例
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../data/lena512g.bmp", 0)
temp = cv.imread("../../data/temp.bmp", 0)

h, w = temp.shape

# 越大，越匹配
match_result = cv.matchTemplate(img, temp, cv.TM_CCOEFF)

minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(match_result)

topLeft = maxLoc

bottomRight = (topLeft[0] + w, topLeft[1] + h)

rst = cv.rectangle(img, topLeft, bottomRight, 255, 3)

cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()
