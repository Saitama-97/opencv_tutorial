# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.08.30 09:21 
  @File    : xor1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像加解密 - 异或(xor)
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/lena.jpg")
w, h, c = img.shape
key = np.random.randint(0, 256, size=[w, h, c], dtype=np.uint8)
encoded_img = cv.bitwise_xor(img, key)

cv.imshow("img", img)
cv.imshow("key", key)
cv.imshow("encoded", encoded_img)

decoded_img = cv.bitwise_xor(encoded_img, key)
cv.imshow("decoded", decoded_img)

cv.waitKey()
cv.destroyAllWindows()
