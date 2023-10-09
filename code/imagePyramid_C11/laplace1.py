# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.09 11:59
  @File    : laplace1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 拉普拉斯金字塔 - 高斯金字塔中的第 i 层与高斯金字塔中的第 i+1 层的向上采样结果之差
            应用在于，能够恢复高分辨率的图像
"""

import cv2 as cv

img = cv.imread("../../data/lena.bmp")

G0 = img
G1 = cv.pyrDown(G0)
G2 = cv.pyrDown(G1)
G3 = cv.pyrDown(G2)

L0 = G0 - cv.pyrUp(G1)
L1 = G1 - cv.pyrUp(G2)
L2 = G2 - cv.pyrUp(G3)

print("L0.shape=", L0.shape)
print("L1.shape=", L1.shape)
print("L2.shape=", L2.shape)

cv.imshow("L0", L0)
cv.imshow("L1", L1)
cv.imshow("L2", L2)

cv.waitKey()
cv.destroyAllWindows()
