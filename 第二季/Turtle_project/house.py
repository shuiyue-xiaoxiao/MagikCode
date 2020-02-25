import turtle
import time
t = turtle.Pen()
t.color('green','red')
t.hideturtle()

t.begin_fill()
for x in range(3):
    t.forward(100)
    t.left(180-60)
t.forward(10)
t.right(90)
t.end_fill()
t.color('green','brown')
t.begin_fill()
for x in range(3):
    t.forward(80)
    t.left(90)
t.end_fill()
t.penup()
t.goto(30,-80)
t.pendown()
for x in range(3):
    t.right(90)
    t.forward(40)

time.sleep(20)
