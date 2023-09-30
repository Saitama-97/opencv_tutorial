# _*_ coding: utf-8 _*_

"""
  @Time    : 2023/9/30 10:19 
  @File    : topHat2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像形态学操作 - 礼帽操作
            可以获取图像的噪声信息，或者得到比原始图像的边缘更亮的边缘信息
"""

import numpy as np
import cv2 as cv

img_raw_1 = cv.imread("../../data/lena.bmp")

k = np.ones((5, 5), dtype=np.uint8)

img_rst_1 = cv.morphologyEx(img_raw_1, cv.MORPH_TOPHAT, kernel=k)

cv.imshow("raw1", img_raw_1)
cv.imshow("rst1", img_rst_1)

cv.waitKey()
cv.destroyAllWindows()
