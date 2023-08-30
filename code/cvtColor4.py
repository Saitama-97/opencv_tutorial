# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 14:30 
  @File    : cvtColor4.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 色彩空间转换 - cv.cvtColor()
"""

import cv2 as cv
import numpy as np

img = cv.imread("../data/lena.jpg")

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("img", img)
cv.imshow("rgb", rgb)

cv.waitKey()
cv.destroyAllWindows()
