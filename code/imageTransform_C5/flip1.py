# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 16:26 
  @File    : flip1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像翻转 - cv.flip(raw_img, flipMode)
            flipMode:
                    0 - x 轴
                    正数 - y 轴
                    负数 - x、y 轴
"""

import cv2 as cv

img = cv.imread("../../data/lena.bmp")

# x 轴翻转
rst1 = cv.flip(img, 0)
# y 轴翻转
rst2 = cv.flip(img, 1)
# x、y 轴翻转
rst3 = cv.flip(img, -1)

cv.imshow("raw", img)
cv.imshow("x axis", rst1)
cv.imshow("y axis", rst2)
cv.imshow("x and y axis", rst3)

cv.waitKey()
cv.destroyAllWindows()
