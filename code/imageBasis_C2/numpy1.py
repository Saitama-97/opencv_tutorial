import cv2
import numpy as np

img = np.zeros((8, 8), dtype=np.int8)
print("img=\n", img)

cv2.imshow('one', img)

print("读取像素点img[0,3]=", img[0, 3])

img[0, 3] = 255  # 修改像素点

cv2.imshow('two', img)

cv2.waitKey()
cv2.destroyAllWindows()
