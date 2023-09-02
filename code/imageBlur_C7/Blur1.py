# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.02 09:42 
  @File    : Blur1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像平滑处理 - 均值滤波 - cv.blur(img, ksize, anchor, borderType)
            ksize : 滤波核大小
            anchor : 锚点，默认为(-1, -1)，表示为核的中心点，一般保持默认值即可
            borderType : 边界样式，一般保持默认值即可
            综上所述：
            cv.blur(img, ksize)
"""

import numpy as np
import cv2 as cv

img = cv.imread("../../data/lena.jpg")

dst1 = cv.blur(img, (5, 5))
dst2 = cv.blur(img, (30, 30))

cv.imshow("img", img)
cv.imshow("dst1", dst1)
cv.imshow("dst2", dst2)

cv.waitKey()
cv.destroyAllWindows()
