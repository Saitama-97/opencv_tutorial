import cv2 as cv
import numpy as np

img = np.zeros((2, 4, 3), dtype=np.uint8)

print(img)

print("img[0,3] = ", img[0, 3])
print("img[1,2,2] = ", img[1, 2, 2])

img[0, 3] = 255
img[1, 2, 2] = 4

print("img[0,3] = ", img[0, 3])
print("img[1,2,2] = ", img[1, 2, 2])
