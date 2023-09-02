import cv2 as cv

img = cv.imread('../../data/lena.bmp')
cv.imshow('lena_before', img)

for i in range(10, 100):
    for j in range(80, 100):
        img[i, j] = 255

cv.imshow('lena_after', img)

cv.waitKey()
cv.destroyAllWindows()
