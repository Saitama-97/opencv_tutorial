import numpy as np
import cv2 as cv

"""
图像加法 +、cv.add()
"""

img1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
img2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)

print("img1=\n", img1)
print("img2=\n", img2)

img3 = img1 + img2

print("img3=\n", img3)

img4 = cv.add(img1, img2)

print("img4=\n", img4)


