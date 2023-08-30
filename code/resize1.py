# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 16:03 
  @File    : resize1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像缩放 - cv.resize()
  shape - (h, w ,c)
  dsize - (w, h)
  需要注意
"""

import numpy as np
import cv2 as cv

img = np.ones([2, 4, 3], dtype=np.uint8)

size = img.shape[:2]

rst = cv.resize(img, size)

# original image - 2 x 4
print(size)
# after process - 4 x 2
print(rst.shape[:2])
