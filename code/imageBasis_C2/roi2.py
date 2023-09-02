import numpy as np
import cv2 as cv

"""
操作ROI
"""

img = cv.imread("../../data/lena.jpg")

face = np.random.randint(0, 256, size=[180, 100, 3], dtype=np.uint8)
img[220:400, 250:350] = face

cv.imshow("original", img)

cv.waitKey()
cv.destroyAllWindows()
