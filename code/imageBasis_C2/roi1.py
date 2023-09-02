import numpy as np
import cv2 as cv

"""
读取ROI
"""

img = cv.imread("../../data/lena.jpg")

face = img[220:400, 250:350]

cv.imshow("original", img)
cv.imshow("face", face)

cv.waitKey()
cv.destroyAllWindows()
