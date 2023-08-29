import cv2 as cv
import numpy as np

img = np.random.randint(10, 99, size=[5, 5], dtype=np.uint8)
print("img=\n", img)

print("Before, img[3,2]=", img.item(3, 2))

img.itemset((3, 2), 98)

print("After, img[3,2]=", img.item(3, 2))
