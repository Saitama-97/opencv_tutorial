# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.09 10:35
  @File    : pyrUpAndDown.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 采样的不可逆性 - 一幅图片先后经过 下采样 + 上采样（上采样 + 下采样），图片大小不变，肉眼看起来相似，但是实际上像素值不一致
"""

import cv2 as cv

img = cv.imread("../../data/lena.bmp")

downRst = cv.pyrDown(img)
upRst = cv.pyrUp(downRst)
diff = img - upRst

cv.imshow("raw", img)
cv.imshow("down", downRst)
cv.imshow("up", upRst)
cv.imshow("diff", diff)

cv.waitKey()
cv.destroyAllWindows()
