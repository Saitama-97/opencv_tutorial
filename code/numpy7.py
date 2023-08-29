import cv2 as cv
import numpy as np

"""
随机生成一幅灰度图/彩色图
"""

img_gray = np.random.randint(0, 256, size=[256, 256], dtype=np.uint8)
img_color = np.random.randint(0, 256, size=[256, 256, 3], dtype=np.uint8)

cv.imshow("img_gray", img_gray)
cv.imshow("img_color", img_color)

cv.waitKey()
cv.destroyAllWindows()
