# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.16 11:00
  @File    : houghLinesP1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 概率霍夫变换 - cv.houghLinesP()
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# -1：原图
# 0：灰度图
# 1：RGB
img = cv.imread("../../data/computer.jpg", -1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(img, 50, 150, apertureSize=3)
orgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
oshow = orgb.copy()

lines = cv.HoughLinesP(edges, 1, np.pi / 180, 1, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(orgb, (x1, y1), (x2, y2), (255, 0, 0), 5)

plt.subplot(121)
plt.imshow(oshow)
plt.axis("off")

plt.subplot(122)
plt.imshow(orgb)
plt.axis("off")

plt.show()