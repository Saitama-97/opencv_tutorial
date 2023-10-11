# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.11 10:15
  @File    : plot1.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : pyplot 实例
"""

import matplotlib.pyplot as plt

a = [0.3, 0.4, 2, 5, 3, 4.5, 4]
b = [3, 5, 1, 2, 1, 5, 3]

plt.plot(a, color='r')
plt.plot(b, color='b')

plt.show()
