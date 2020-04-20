from turtle import *

x_width = 1200
y_height = 800

speed(8)

setup(x_width, y_height)
title('Flag Of China')


def pen_goto(a, b):
    penup()
    goto(a, b)
    pendown()


def coordinate_axis():
    pen_goto(- x_width / 2, 0)
    forward(x_width)
    pen_goto(0, - y_height / 2)
    setheading(90)
    forward(y_height)


def ref_rowLine():
    x_start = - x_width / 2
    y_start = y_height / 2
    print('x坐标')
    for i in range(10):
        pen_goto(x_start, y_start)
        setheading(0)
        forward(x_width / 2)
        y_start -= 40
        print(y_start)
        print('!@!@!@!@!@!@!@!@!@!@!@!@!@!')

    print('y坐标')
    for i in range(15):
        pen_goto(x_start, y_start)
        setheading(90)
        forward(x_width / 2)
        x_start += 40
        print(x_start)
        print('!@!@!@!@!@!@!@!@!@!@!@!@!@!')


ht()
coordinate_axis()
ref_rowLine()
mainloop()
