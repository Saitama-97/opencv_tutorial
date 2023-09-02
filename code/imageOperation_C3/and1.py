import cv2 as cv
import numpy as np

img1 = np.random.randint(0, 255, (5, 5), dtype=np.uint8)
img2 = np.zeros((5, 5), dtype=np.uint8)

img2[0:3, 0:3] = 255
img2[4, 4] = 255

img3 = cv.bitwise_and(img1, img2)

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("img3", img3)

cv.waitKey()
cv.destroyAllWindows()
