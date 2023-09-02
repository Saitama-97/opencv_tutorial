import numpy as np
import cv2 as cv

"""
通道拆分 - cv.split()
"""

img = cv.imread("../../data/lena.jpg")

# Blue Channel
blue = img[:, :, 0]
# Green Channel
green = img[:, :, 1]
# Red Channel
red = img[:, :, 2]

cv.imshow("b", blue)
cv.imshow("g", green)
cv.imshow("r", red)

img[:, :, 0] = 0
cv.imshow("x", img)

img[:, :, 1] = 0
cv.imshow("y", img)

cv.waitKey()
cv.destroyAllWindows()
