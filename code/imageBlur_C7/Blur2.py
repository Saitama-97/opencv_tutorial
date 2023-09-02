# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.09.02 09:52 
  @File    : Blur2.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Des     : 图像平滑处理 - 方框滤波 - cv.boxFilter(img, ddepth, ksize, anchor, normalize, borderType)
            ddepth : 表示处理结果图像的深度，一般使用 -1 表示和源图像使用相同的图像深度
            ksize : 滤波核
            anchor : 锚点，一般使用默认值(-1, -1)
            normalize : 是否归一化【是：采用邻域像素值之和的平均值 | 否：采用邻域像素值之和】
            borderType : 边界样式，一般使用默认值
            综上所述：
            cv.boxFilter(img, ksize, normalize)
"""

import cv2 as cv
import numpy as np

img = cv.imread("../../data/lenaNoise.png")
blur = cv.blur(img, (5, 5))
box_with_normalize = cv.boxFilter(img, ddepth=-1, ksize=(5, 5), normalize=True)
box_without_normalize = cv.boxFilter(img, ddepth=-1, ksize=(5, 5), normalize=False)

cv.imshow("img", img)
cv.imshow("blur", blur)
cv.imshow("box_with_normalized", box_with_normalize)
cv.imshow("box_without_normalized", box_without_normalize)

cv.waitKey()
cv.destroyAllWindows()
