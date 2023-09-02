# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.01 09:34 
  @File    : threshold2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 阈值处理 - cv.threshold(img, thresh, maxval, type)
            反二值化处理 - type: cv.THRESH_BINARY_INV
            大于阈值置为 0
            小于阈值置为 maxval
"""

import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)

ret, rst = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_BINARY_INV)

print("img=\n", img)
print(ret)
print("rst=\n", rst)
