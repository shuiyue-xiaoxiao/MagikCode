from turtle import *

x_width = 1200
y_height = 800

bgcolor('red')


def flag_loop():
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
        print('y坐标')
        for i in range(10):
            pen_goto(x_start, y_start)
            setheading(0)
            forward(x_width / 2)
            y_start -= 40
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
        pencolor('yellow')
        pen_goto(- x_width / 2 / 15 * 10, y_height / 2 / 10 * 2)
        setheading(0)
        circle(x_width / 2 / 15 * 3)

    def pos_star():
        pencolor('yellow')
        pen_goto(- x_width / 2 / 15 * 5, y_height / 2 / 10 * 7)
        circle(x_width / 2 / 15)
        pen_goto(- x_width / 2 / 15 * 3, y_height / 2 / 10 * 5)
        circle(x_width / 2 / 15)
        pen_goto(- x_width / 2 / 15 * 3, y_height / 2 / 10 * 2)
        circle(x_width / 2 / 15)
        pen_goto(- x_width / 2 / 15 * 5, y_height / 2 / 10 * 0)
        circle(x_width / 2 / 15)

    def link_line():
        pen_goto(- x_width / 2 / 15 * 10, y_height / 2 / 10 * 5)
        goto(- x_width / 2 / 15 * 5, y_height / 2 / 10 * 8)
        pen_goto(- x_width / 2 / 15 * 10, y_height / 2 / 10 * 5)
        goto(- x_width / 2 / 15 * 3, y_height / 2 / 10 * 6)
        pen_goto(- x_width / 2 / 15 * 10, y_height / 2 / 10 * 5)
        goto(- x_width / 2 / 15 * 3, y_height / 2 / 10 * 3)
        pen_goto(- x_width / 2 / 15 * 10, y_height / 2 / 10 * 5)
        goto(- x_width / 2 / 15 * 5, y_height / 2 / 10 * 1)

    coordinate_axis()
    ref_rowLine()
    pos_BigStar()
    link_line()
    pos_star()


speed(0)
setup(x_width, y_height)
title('Flag Of China')
ht()
flag_loop()
mainloop()
