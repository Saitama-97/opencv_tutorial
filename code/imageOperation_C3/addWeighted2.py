import cv2 as cv
import numpy as np

"""
图像加权和 - cv.addWeighted(img1, alpha, img2, beta, gamma)
img1*alpha + img2*beta + gamma
# img1 和 img2 必须 大小（shape）类型（dtype）相同
"""

img1 = cv.imread("../../data/boat.bmp")
# img1 need to reshape
new_img1 = img1[:512, :512]
img2 = cv.imread("../../data/lena.bmp")

img3 = cv.addWeighted(new_img1, 0.6, img2, 0.4, 0)

cv.imshow("boat", new_img1)
cv.imshow("lena", img2)
cv.imshow("boat+lena", img3)

cv.waitKey()
cv.destroyAllWindows()
