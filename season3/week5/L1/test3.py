from turtle import *
# speed(0)


def pen_goto(x, y):
    penup()
    goto(x, y)
    pendown()


'''头'''
hideturtle()
pen_goto(0, 70)
dot(50, 'black')

'''身子'''
pensize(5)
setheading(270)
forward(100)

'''胳膊'''
setheading(90)
forward(65)
left(120)
forward(55)
left(110)
forward(40)
left(180)
forward(40)
right(110)
forward(55)
setheading(90)
right(85)
forward(40)
left(20)
forward(40)
right(180)
forward(40)
right(20)
forward(40)

'''腿'''
setheading(90)
backward(75)
left(140)
forward(40)
left(20)
forward(40)
left(180)
forward(40)
right(20)
forward(40)
setheading(90)
right(80)
forward(40)
right(20)
forward(40)
right(180)
forward(40)
left(20)
forward(40)

mainloop()
