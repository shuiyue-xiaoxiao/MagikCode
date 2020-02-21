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

#画第一个五角星
penup()
goto(-600, 260)
right(0)
pendown()

begin_fill()
for i in range(5):
    forward(70)
    left(72)
    forward(70)
    right(144)
end_fill()

#画第二个五角星
penup()
goto(-360, 340)
right(18)
pendown()

begin_fill()
for i in range(5):
    forward(25)
    left(72)
    forward(25)
    right(144)
end_fill()

#画第三个五角星
penup()
goto(-300, 260)
right(-36)
pendown()

begin_fill()
for i in range(5):
    forward(25)
    left(72)
    forward(25)
    right(144)
end_fill()

#画第四个五角星
penup()
goto(-300, 180)
right(18)
pendown()

begin_fill()
for i in range(5):
    forward(25)
    left(72)
    forward(25)
    right(144)
end_fill()

#画第五个五角星
penup()
goto(-360, 110)
right(18)
pendown()

begin_fill()
for i in range(5):
    forward(25)
    left(72)
    forward(25)
    right(144)
end_fill()
#结束

