# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.01 10:16 
  @File    : threshold6.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 自适应阈值处理 - cv.adaptiveThreshold()
"""

import cv2 as cv
import numpy as np

# grayscale image
img = cv.imread("../../data/lena.jpg", 0)

ret, rst = cv.threshold(img, 127, 255, type=cv.THRESH_BINARY)

adap_mean_rst = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 3)

adap_gauss_rst = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 3)

cv.imshow("raw", img)
cv.imshow("normal", rst)
cv.imshow("mean", adap_mean_rst)
cv.imshow("gauss", adap_gauss_rst)

cv.waitKey()
cv.destroyAllWindows()
