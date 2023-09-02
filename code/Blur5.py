# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.02 10:45 
  @File    : Blur5.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像平滑处理 - 双边滤波 - cv.bilateralFilter(img, d, sigmaColor, sigmaSpace)
            d : 滤波时选取的空间距离参数，表示以当前像素点为中心点的直径，推荐 5，对于较大噪声，推荐 9
            sigmaColor : 滤波时选取的颜色差值范围，决定周围多少像素点参与进来
            sigmaSpace : 一般同上
"""

import cv2 as cv
import numpy as np

img = np.ones((300, 500), dtype=np.uint8)
img[:, :250] = 0
img[:, 250:] = 255

# 均值滤波
blur = cv.blur(img, ksize=(5, 5))
# 方框滤波
box = cv.boxFilter(img, ddepth=-1, ksize=(5, 5), normalize=True)
# 高斯滤波
gauss = cv.GaussianBlur(img, ksize=(5, 5), sigmaY=0, sigmaX=0)
# 中值滤波
median = cv.medianBlur(img, ksize=5)
# 双边滤波
bilateral = cv.bilateralFilter(img, d=25, sigmaColor=100, sigmaSpace=100)

cv.imshow("img", img)
cv.imshow("blur", blur)
cv.imshow("box", box)
cv.imshow("gauss", gauss)
cv.imshow("median", median)
cv.imshow("bilateral", bilateral)

cv.waitKey()
cv.destroyAllWindows()
