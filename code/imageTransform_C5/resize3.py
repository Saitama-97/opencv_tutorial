# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 16:21 
  @File    : resize3.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像缩放 - cv.resize(raw_img, dsize=None, fx, fy)
            注意：fx - 对应着 h
                 fy - 对应着 w
            与 shape 是反的
"""

import cv2 as cv

img = cv.imread("../../data/lena.bmp")

print(img.shape[:2])
rst = cv.resize(img, dsize=None, fx=2, fy=0.5)
print(rst.shape[:2])
