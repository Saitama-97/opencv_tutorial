import numpy as np
import cv2 as cv

"""
获取图像属性
"""

img_gray = cv.imread("../data/lena.bmp")
img_color = cv.imread("../data/lena.jpg")

print("img_gray 属性")
print("shape=", img_gray.shape)
print("size=", img_gray.size)
print("dtype=", img_gray.dtype)
print()
print("img_color 属性")
print("shape=", img_color.shape)
print("size=", img_color.size)
print("dtype=", img_color.dtype)

cv.waitKey()
cv.destroyAllWindows()
