# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.16 11:41
  @File    : houghCircles1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 霍夫变换检测图像中的圆 - cv.HoughCircles()
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_origin = cv.imread("../../data/chess.jpg", -1)
img_gray = cv.imread("../../data/chess.jpg", 0)

o = cv.cvtColor(img_origin, cv.COLOR_BGR2GRAY)

oshow = o.copy()

img = cv.medianBlur(img_gray, 5)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 300, param1=50, param2=30, minRadius=100, maxRadius=200)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv.circle(o, (i[0], i[1]), i[2], (255, 0, 0), 12)
    cv.circle(o, (i[0], i[1]), 2, (255, 0, 0), 12)
plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')
plt.subplot(122)
plt.imshow(o)
plt.axis('off')
