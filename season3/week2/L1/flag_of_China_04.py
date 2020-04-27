from turtle import *
from math import *

x_width = 1200
y_height = 800
bgcolor('#DE2910')


def flag_loop():
    def pen_goto(a, b):
        penup()
        goto(a, b)
        pendown()

    def coordinate_axis():
        speed(0)
        pen_goto(- x_width / 2, 0)
        forward(x_width)
        pen_goto(0, - y_height / 2)
        setheading(90)
        forward(y_height)

    square_size = x_width / 2 / 15  # y_width / 2 / 10

    def ref_rowLine():
        speed(0)
        x_start = - x_width / 2
        y_start = y_height / 2
        print('y坐标')
        for i in range(10):
            pen_goto(x_start, y_start)
            setheading(0)
            forward(x_width / 2)
            y_start -= y_height / 2 / 10
            print(y_start)
            print('!@!@!@!@!@!@!@!@!@!@!@!@!@!')

        print('x坐标')
        for i in range(15):
            pen_goto(x_start, y_start)
            setheading(90)
            forward(x_width / 2)
            x_start += 40
            print(x_start)
            print('!@!@!@!@!@!@!@!@!@!@!@!@!@!')

    def pos_BigStar():
        speed(0)
        pencolor('yellow')
        pen_goto(- square_size * 10, square_size * 2)
        setheading(0)
        circle(square_size * 3)

    def pos_star():
        speed(0)
        pencolor('yellow')
        pen_goto(- square_size * 5, square_size * 7)
        circle(x_width / 2 / 15)
        pen_goto(- square_size * 3, square_size * 5)
        circle(x_width / 2 / 15)
        pen_goto(- square_size * 3, square_size * 2)
        circle(x_width / 2 / 15)
        pen_goto(- square_size * 5, square_size * 0)
        circle(square_size)

    def link_line():
        speed(0)
        pen_goto(- square_size * 10, square_size * 5)
        goto(- square_size * 5, square_size * 8)
        pen_goto(- square_size * 10, square_size * 5)
        goto(- square_size * 3, square_size * 6)
        pen_goto(- square_size * 10, square_size * 5)
        goto(- square_size * 3, square_size * 3)
        pen_goto(- square_size * 10, square_size * 5)
        goto(- square_size * 5, square_size * 1)

    def bigStar():
        color('yellow')
        speed(5)
        pen_goto(- square_size * 10, square_size * 8)
        setheading(-72)
        side_length = sin(radians(36)) / cos(radians(36)) * (square_size * 3)
        begin_fill()
        for i in range(5):
            forward(side_length)
            left(72)
            forward(side_length)
            right(144)
        end_fill()

    coordinate_axis()
    ref_rowLine()
    pos_BigStar()
    pos_star()
    link_line()
    bigStar()


setup(x_width, y_height)
title('Flag Of China')
ht()
flag_loop()
mainloop()
