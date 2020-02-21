 # 中华人民共和国国旗
from turtle import *

# 设置窗口(宽度，高度，x起点，y起点)
setup(width=1440, height=900, startx=0, starty=0)

# 设置背景颜色
bgcolor("red")

pensize(0)
        

# 设置画笔颜色
pencolor("yellow")
# 设置填充颜色
fillcolor("yellow")

speed(5)

def draw_star(startx, starty, angle, pixel):
    penup()
    goto(startx, starty)
    right(angle)
    pendown()

    begin_fill()
    for i in range(5):
        forward(pixel)
        left(72)
        forward(pixel)
        right(144)
    end_fill()
    
# 画第一个五角星
draw_star(startx=-600, starty=260, angle=0, pixel=70)
# 画第二个五角星
draw_star(startx=-360, starty=340, angle=18, pixel=25)
# 画第三个五角星
draw_star(startx=-300, starty=260, angle=-36, pixel=25)
# 画第四个五角星
draw_star(startx=-300, starty=180, angle=18, pixel=25)
# 画第五个五角星
draw_star(startx=-360, starty=110, angle=18, pixel=25)
