# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.01 09:21 
  @File    : threshold1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 阈值处理 - cv.threshold(img, thresh, maxval, type)
            二值化处理 - type: cv.THRESH_BINARY
            大于阈值置为 maxval
            小于阈值置为 0
"""

import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)

ret, rst = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

print("img=\n", img)
print(ret)
print("rst=\n", rst)
