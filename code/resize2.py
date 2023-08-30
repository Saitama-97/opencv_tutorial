# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 16:13 
  @File    : resize2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像缩放 - cv.resize(raw_img,dsize=(w, h))
"""

import cv2 as cv
import numpy as np

img = cv.imread("../data/lena.bmp")
h, w = img.shape[:2]

rst = cv.resize(img, dsize=(int(w * 0.6), int(h * 0.8)))

cv.imshow("image", img)
cv.imshow("result", rst)

cv.waitKey()
cv.destroyAllWindows()
