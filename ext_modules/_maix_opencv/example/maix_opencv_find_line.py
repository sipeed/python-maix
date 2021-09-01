#!/usr/bin/env python

# cv.find_line(pic)函数说明
# 功能:在道路图片pic中寻找线
# 输入：pic，240*240尺寸的图片bytes数据
# 返回值：字典类型，rect：矩形的四个顶点，pixels：矩形的面积，cx、cy:矩形的中心坐标，rotation：矩形的倾斜角
#{'rect': [9, 229, 9, 9, 145, 9, 145, 229], 'pixels': 12959, 'cx': 77, 'cy': 119, 'rotation': -1.570796251296997}

from maix import camera
from _maix_opencv import _v83x_opencv
from PIL import Image ,ImageDraw
from maix import display
cv = _v83x_opencv()

#跳过一些帧
tmp = camera.read()
tmp = camera.read()
tmp = camera.read()
tmp = camera.read()
tmp = camera.read()
tmp = camera.read()
tmp = camera.read()
tmp = camera.read()
tmp = camera.read()

def find_line():
  while True:
    tmp = camera.read()
    if tmp:
      ma = cv.find_line(tmp)
      print(ma)
      draw = display.get_draw()
      draw.line([(ma["rect"][0], ma["rect"][1]), (ma["rect"][2], ma["rect"][3])],fill='white',width=1)
      draw.line([(ma["rect"][2], ma["rect"][3]), (ma["rect"][4], ma["rect"][5])],fill='white',width=1)
      draw.line([(ma["rect"][4], ma["rect"][5]), (ma["rect"][6], ma["rect"][7])],fill='white',width=1)
      draw.line([(ma["rect"][6], ma["rect"][7]), (ma["rect"][0], ma["rect"][1])],fill='white',width=1)
      draw.ellipse(((ma["cx"]-2, ma["cy"]-2), (ma["cx"]+2, ma["cy"]+2)), fill=None, width=1)
      display.show()
if __name__ == "__main__":
  find_line()