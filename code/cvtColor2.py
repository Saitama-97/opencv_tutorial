# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 11:53 
  @File    : cvtColor2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 色彩空间转换 - cv.cvtColor()
"""

import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[512, 512], dtype=np.uint8)

rst = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

cv.imshow("img", img)
cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()
