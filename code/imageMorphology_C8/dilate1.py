# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.12 09:42
  @File    : dilate1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像形态学操作 - 膨胀 - cv.dilate()
"""

import cv2 as cv
import numpy as np

img = np.zeros((5, 5), dtype=np.uint8)

img[1, 1:4] = 1

kernel = np.ones((3, 1), dtype=np.uint8)

rst = cv.dilate(img, kernel)

print("img=\n", img)
print("rst=\n", rst)
