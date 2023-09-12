# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.12 09:49
  @File    : open1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像形态学运算 - 开运算 - 先腐蚀再膨胀
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/opening.bmp")

kernel = np.ones((10, 10), dtype=np.uint8)

rst = cv.morphologyEx(img, op=cv.MORPH_OPEN, kernel=kernel)

cv.imshow("img", img)
cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()
