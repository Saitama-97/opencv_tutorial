# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.12 09:33
  @File    : match3.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 多模板匹配
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../data/lena4.bmp", 0)

template = cv.imread("../../data/lena4Temp.bmp", 0)

w, h = template.shape

match_rst = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

threshold = 0.9

loc = np.where(match_rst > threshold)

for pt in zip(*loc[::-1]):
    img = cv.rectangle(img, pt, (pt[0] + w, pt[0] + h), 255, 2)
    cv.imshow("rst", img)

cv.waitKey()
cv.destroyAllWindows()
