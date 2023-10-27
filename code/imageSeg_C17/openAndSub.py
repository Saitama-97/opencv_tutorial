# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.17 14:50
  @File    : openAndSub.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 开运算 + 减法运算，获取图像的边界
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

o = cv.imread("../../data/my.bmp")

k = np.ones((5, 5), np.uint8)

e = cv.erode(o, k)
b = cv.subtract(o, e)

plt.subplot(131)
plt.imshow(o)
plt.axis("off")

plt.subplot(132)
plt.imshow(e)
plt.axis("off")

plt.subplot(133)
plt.imshow(b)
plt.axis("off")

plt.show()

