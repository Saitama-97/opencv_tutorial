import cv2 as cv
import numpy as np

img = np.zeros((300, 300, 3), dtype=np.uint8)

img[:, 0:100, 0] = 255
img[:, 100:200, 1] = 255
img[:, 200:300, 2] = 255

cv.imshow('img', img)
print(img)

cv.waitKey()
cv.destroyAllWindows()
