# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.12 09:26
  @File    : erode1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 图像形态学操作 - 腐蚀 - cv.erode()
"""

import cv2 as cv
import numpy as np

img = np.zeros((5, 5), dtype=np.uint8)

kernel = np.ones((3, 1), dtype=np.uint8)

img[1:4, 1:4] = 1
rst = cv.erode(img, kernel)

print("img=\n", img)
print("rst=\n", rst)

# 21-22
# 8000*12+12000+30000 = 138000
# 9700*12+12000+30000 = 158400

# 22-23
# 10000*12+12000+30000 = 162000
# 11700*12+12000+30000 = 182400

# 23-24
# 11000*12+12000+30000 = 174000
# 12700*12+12000+30000 = 194400

# 24-25
# 12000*12+12000+28000 = 184000
# 13700*12+12000+28000 = 204400

# 25-26
# 16700*12+12000 =
