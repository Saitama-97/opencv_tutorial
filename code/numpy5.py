import cv2 as cv
import numpy as np

img = cv.imread('../data/lena.jpg')
cv.imshow("img_before", img)

for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            img[i, j, k] = 255

for i in range(50, 100):
    for j in range(0, 100):
        for k in range(0, 3):
            img[i, j, k] = 128

for i in range(100, 150):
    for j in range(0, 100):
        for k in range(0, 3):
            img[i, j, k] = 0

cv.imshow("img_after", img)

cv.waitKey()
cv.destroyAllWindows()
