# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 11:57 
  @File    : cvtColor3.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 色彩空间转换 - cv.cvtColor()
"""

import numpy as np
import cv2 as cv

# bgr image
img = np.random.randint(0, 256, size=[512, 512, 3], dtype=np.uint8)

rst = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("img", img)
cv.imshow("rst", rst)

cv.waitKey()
cv.destroyAllWindows()

