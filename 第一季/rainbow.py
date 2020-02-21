turtle = None
screen = None
colours = None
i = None


from turtle import *
turtle = Turtle()
turtle.speed(100)
screen = Screen()
screen.bgcolor("black")
colours = ["red", "purple", "blue", "green", "orange", "yellow"]
for i in range(360):
  turtle.color(colours[i % 6])
  turtle.width(i / 100 + 1)
  turtle.forward(i)
  turtle.left(59)
