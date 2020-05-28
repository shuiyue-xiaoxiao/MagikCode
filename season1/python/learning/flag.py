"""中国国旗"""
from turtle import *

y_height = numinput(" Window Settings",
                    "Please enter the height of the window",
                    800,
                    0,
                    800)  # 国旗正确比例是3:2
x_width = y_height / 2 * 3
setup(x_width, y_height)
title(textinput('the title of works', 'the title of works', ))
square_size = x_width / 2 / 15


def pen_goto(x, y):  # 定义无痕移动画笔
    penup()
    goto(x, y)
    pendown()


def axis():
    speed(5)
    pen_goto(- x_width / 2, 0)
    setheading(0)
    forward(x_width)
    pen_goto(0, - y_height / 2)
    setheading(90)
    forward(y_height)


def ref_line():
    speed(10)
    x_star = - x_width / 2
    y_star = y_height / 2
    setheading(0)
    for i in range(10):
        pen_goto(x_star, y_star)
        forward(x_width / 2)
        y_star = y_star - square_size

    setheading(90)
    for i in range(15):
        pen_goto(x_star, y_star)
        forward(x_width / 2)
        x_star = x_star + square_size


x = x_width / 2 / 10
y = y_height / 2 / 1.4
font_size = int(square_size * 25 / 40)
pen_goto(x, y)
write('step1: Draw the axis', True, align='left', font=('Ariel', font_size, 'normal'))
axis()
ref_line()
mainloop()
