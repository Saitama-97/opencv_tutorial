# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.31 11:29 
  @File    : remap3.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 重映射之复制图像 - cv.remap()
"""

import numpy as np
import cv2 as cv

img = cv.imread("../data/lena.bmp")

h, w = img.shape[:2]

mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)

for i in range(h):
    for j in range(w):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)

rst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)

cv.imshow("raw", img)
cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()
