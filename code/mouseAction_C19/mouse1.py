# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.27 16:45
  @File    : mouse1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 鼠标行为 - cv.onMouseAction()
"""

import cv2
import numpy as np


def demo(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("单击了鼠标左键")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("单击了鼠标右键")
    elif event == cv2.EVENT_FLAG_LBUTTON:
        print("按住右键拖动了鼠标")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print("单击了鼠标中键")


if __name__ == '__main__':
    # 全白图片
    img = np.ones((300, 300, 3), np.uint8) * 255
    cv2.namedWindow("Mouse Demo")
    cv2.setMouseCallback("Mouse Demo", demo)
    cv2.imshow("Mouse Demo", img)

    cv2.waitKey()
    cv2.destroyAllWindows()
