from turtle import *
from math import *
from time import sleep

x_width = numinput("窗口设置", "再次输入窗口的宽度", 1200, 300, 1200)  # 国旗正确比例是3:2
y_height = x_width * 2 / 3

bgcolor('#DE2910')
setup(x_width, y_height)
title(textinput('title', '请输入标题 '))


def pen_goto(a, b):  # 设置无痕移动画笔
    penup()
    goto(a, b)
    pendown()


def coordinate_axis():
    pencolor('black')
    speed(5)
    pen_goto(- x_width / 2, 0)
    forward(x_width)
    pen_goto(0, - y_height / 2)
    setheading(90)
    forward(y_height)


square_size = x_width / 2 / 15  # y_width / 2 / 10


def ref_rowLine():
    fillcolor('black')
    pencolor('black')
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
    speed(5)
    pencolor('black')
    pen_goto(- square_size * 10, square_size * 2)
    setheading(0)
    circle(square_size * 3)


def pos_star():
    speed(5)
    pencolor('black')
    pen_goto(- square_size * 5, square_size * 7)
    circle(x_width / 2 / 15)
    pen_goto(- square_size * 3, square_size * 5)
    circle(x_width / 2 / 15)
    pen_goto(- square_size * 3, square_size * 2)
    circle(x_width / 2 / 15)
    pen_goto(- square_size * 5, square_size * 0)
    circle(square_size)


def link_line():
    speed(5)
    pen_goto(- square_size * 10, square_size * 5)
    goto(- square_size * 5, square_size * 8)
    pen_goto(- square_size * 10, square_size * 5)
    goto(- square_size * 3, square_size * 6)
    pen_goto(- square_size * 10, square_size * 5)
    goto(- square_size * 3, square_size * 3)
    pen_goto(- square_size * 10, square_size * 5)
    goto(- square_size * 5, square_size * 1)


def bigStar():
    fillcolor('yellow')
    pencolor('yellow')
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


def spin(radius, degree):  # 定义弧形移动画笔，参数为"半径"和"度数"
    penup()
    circle(radius, degree)
    pendown()


'''第一个小五角星相对大五角星的夹角:'''
a1 = 3  # 对边
b1 = 5  # 邻边
degree1 = degrees(atan(a1 / b1))
print('第一个小五角星相对大五角星的夹角为：', round(degree1, 1), '度')


def star1():
    fillcolor('yellow')
    pencolor('yellow')
    speed(5)
    pen_goto(- square_size * 5, square_size * 9)
    setheading(0)
    radius = square_size
    degrees = 90 + degree1
    spin(- radius, - degrees)  # 弧形移动画笔
    setheading(degree1 + 18)
    side_length = sin(radians(36)) / cos(radians(36)) * square_size
    begin_fill()
    for i in range(5):
        forward(side_length)
        left(72)
        forward(side_length)
        right(144)
    end_fill()


'''第二个小五角星相对大五角星的夹角:'''
a2 = 1  # 对边
b2 = 7  # 邻边
degree2 = degrees(atan(a2 / b2))
print('第二个小五角星相对大五角星的夹角为：', round(degree2, 1), '度')


def star2():
    fillcolor('yellow')
    pencolor('yellow')
    speed(5)
    pen_goto(- square_size * 3, square_size * 7)
    setheading(0)
    radius = square_size
    degrees = 90 + degree2
    spin(- radius, - degrees)  # 弧形移动画笔
    setheading(degree2 + 18)
    side_length = sin(radians(36)) / cos(radians(36)) * square_size
    begin_fill()
    for i in range(5):
        forward(side_length)
        left(72)
        forward(side_length)
        right(144)
    end_fill()


'''第三个小五角星相对大五角星的夹角:'''
a3 = 2  # 对边
b3 = 7   # 邻边
degree3 = degrees(atan(a3 / b3))
print('第三个小五角星相对大五角星的夹角为：', round(degree3, 1), '度')


def star3():
    fillcolor('yellow')
    pencolor('yellow')
    speed(5)
    pen_goto(- square_size * 3, square_size * 4)
    setheading(0)
    radius = square_size
    degrees = 90 - degree3
    spin(- radius, - degrees)  # 弧形移动画笔
    setheading(- degree3 + 18)
    side_length = sin(radians(36)) / cos(radians(36)) * square_size
    begin_fill()
    for i in range(5):
        forward(side_length)
        left(72)
        forward(side_length)
        right(144)
    end_fill()


'''第四个小五角星相对大五角星的夹角:'''
a4 = 4  # 对边
b4 = 5  # 邻边
degree4 = degrees(atan(a4 / b4))
print('第四个小五角星相对大五角星的夹角为：', round(degree4, 1), '度')


def star4():
    fillcolor('yellow')
    pencolor('yellow')
    speed(5)
    pen_goto(- square_size * 5, square_size * 2)
    setheading(0)
    radius = square_size
    degrees = 90 - degree4
    spin(- radius, - degrees)  # 弧形移动画笔
    setheading(- degree4 + 18)
    side_length = sin(radians(36)) / cos(radians(36)) * square_size
    begin_fill()
    for i in range(5):
        forward(side_length)
        left(72)
        forward(side_length)
        right(144)
    end_fill()


pen_goto(50, 260)
write('step1: Draw axis', True, align='left', font=('Arial', 25, "normal"))
sleep(1)
coordinate_axis()
sleep(1)
pen_goto(50, 220)
write('step2: Draw the upper-left reference line', True, align='left', font=('Arial', 25, "normal"))
sleep(1)
ref_rowLine()
sleep(1)
pen_goto(50, 180)
speed(5)
write('step3: Locate the pentacle', True, align='left', font=('Arial', 25, "normal"))
sleep(1)
pos_BigStar()
pos_star()
link_line()
sleep(1)
pen_goto(50, 140)
write('step4: Draw the big pentacle', True, align='left', font=('Arial', 25, "normal"))
sleep(1)
bigStar()
sleep(1)
pen_goto(50, 100)
pencolor('black')
write('step5: Draw the small pentacle', True, align='left', font=('Arial', 25, "normal"))
sleep(1)
star1()
star2()
star3()
star4()
sleep(1)
sleep(1)
pen_goto(50, 60)
pencolor('black')
write('step6: Add special effects to complete the drawing', True, align='left', font=('Arial', 25, "normal"))
hideturtle()
sleep(1)
clear()
sleep(1)
bigStar()
star1()
star2()
star3()
star4()

bgcolor('#DE2910')


mainloop()
