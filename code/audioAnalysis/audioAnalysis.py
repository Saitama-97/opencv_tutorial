# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.10.24 13:54
  @File    : audioAnalysis.py
  @Project : opencv_tutorial
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 
"""

import wave

wavFile = "E:/无损音乐/莫文蔚 - 这世界那么多人.wav"
f = wave.open(wavFile)
# 音频头 参数
params = f.getparams()
Channels = f.getnchannels()
SampleRate = f.getframerate()
bit_type = f.getsampwidth() * 8
frames = f.getnframes()
# Duration 也就是音频时长 = 采样点数/采样率
Duration = wav_time = frames / float(SampleRate)  # 单位为s

# print("音频头参数：", params)
print("通道数(Channels)：", Channels)
print("采样率(SampleRate)：", SampleRate)
print("比特(Precision)：", bit_type)
print("采样点数(frames)：", frames)
print("帧数或者时间(Duration)：", Duration)

