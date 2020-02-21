# 1-4-4_设置画笔颜色

from turtle import *

# 设置颜色模式
colormode(255)

# 设置画笔颜色1：英文代码
# pencolor("tan")

# 设置画笔颜色2：十六进制颜色码
# pencolor("#4169E1")

# 设置画笔颜色3：RGB颜色值
pencolor(222, 9, 250)

for i in range(4):
    forward(100)
    right(90)

'''
colormode()<颜色模式> 括号内的参数为 1.0 或 255, 默认是 1.0;
1.0 默认模式下，颜色可用 英文代码 或 十六进制颜色码 进行设置;
255 模式下，颜色可用 RGB颜色值 进行设置。
'''
