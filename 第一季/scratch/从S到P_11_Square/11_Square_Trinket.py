from turtle import *
turtle = Turtle()
turtle.shape("turtle")
screen = Screen()
turtle.pencolor(225, 0, 0)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
for i in range(4):
    turtle.forward(200)
    turtle.right(90)