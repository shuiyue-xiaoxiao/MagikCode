# 1-4-5_设置背景颜色

from turtle import *
12345678
# 设置颜色模式
colormode(255)

# 设置背景颜色
bgcolor(65, 105, 225)

# 设置画笔颜色1：英文代码
# pencolor("red")

# 设置画笔颜色2：十六进制颜色码
# pencolor("#FF0000")

# 设置画笔颜色3：RGB颜色值
pencolor(255, 0, 0)

for i in range(4):
    forward(100)
    right(90)

'''
colormode()<颜色模式> 括号内的参数为 1.0 或 255, 默认是 1.0;
1.0 默认模式下，颜色可用 英文代码 或 十六进制颜色码 进行设置;
255 模式下，颜色可用 RGB颜色值 进行设置。
'''
