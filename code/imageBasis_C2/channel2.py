import numpy as np
import cv2 as cv

"""
通道合并 - cv.merge()
"""

img = cv.imread("../../data/lena.jpg")

b, g, r = cv.split(img)

bgr = cv.merge([b, g, r])
rgb = cv.merge([r, g, b])

cv.imshow("bgr", bgr)
cv.imshow("rgb", rgb)

cv.waitKey()
cv.destroyAllWindows()
