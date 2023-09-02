# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.02 10:30 
  @File    : Blur3.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像平滑处理 - 高斯滤波 - cv.GaussianBlur(img, ksize, sigmaX, sigmaY, borderType)
            sigmaX : 卷积核在 X 轴方向的标准差
            sigmaY : 卷积核在 Y 轴方向的标准差
            综上所述：
            cv.GaussianBlur(img, ksize, sigmaX=0, sigmaY=0)
"""

import cv2 as cv

img = cv.imread("../data/lenaNoise.png")

dst = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=0, sigmaY=0)

cv.imshow("img", img)
cv.imshow("GaussianBlur", dst)

cv.waitKey()
cv.destroyAllWindows()
