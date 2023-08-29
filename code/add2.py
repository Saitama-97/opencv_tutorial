import cv2 as cv
import numpy as np

"""
图像加法 +、cv.add()
"""

img = cv.imread("../data/lena.jpg", 0)

cv.imshow("lena", img)

new_img1 = img + img
new_img2 = cv.add(new_img1, new_img1)

cv.imshow("lena+lena", new_img1)
cv.imshow("lena.add", new_img2)

cv.waitKey()
cv.destroyAllWindows()
