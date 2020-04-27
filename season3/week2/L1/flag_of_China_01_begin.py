from turtle import *

x_width = 1200
y_height = 800

speed(0)

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


coordinate_axis()

mainloop()
