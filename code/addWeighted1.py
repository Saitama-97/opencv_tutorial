import cv2 as cv
import numpy as np

"""
图像加权和 - cv.addWeighted(img1, alpha, img2, beta, gamma)
img1*alpha + img2*beta + gamma
"""

img1 = np.ones((3, 4), dtype=np.uint8) * 100
img2 = np.ones((3, 4), dtype=np.uint8) * 10

print("img1=\n", img1)
print("img2=\n", img2)

img3 = cv.addWeighted(img1, 0.6, img2, 5, 3)

print("img3=\n", img3)
