# 1-10-1
# 螺旋彩虹

'''
# (1): 采用了两种变量
from turtle import *

turtle = Turtle()

screen = Screen()

turtle.speed(0)

screen.bgcolor("black")

colours = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
  turtle.color(colours[i % 6])
  turtle.width(i / 100 + 1)
  turtle.forward(i)
  turtle.left(59)
'''

# (2):不采用变量
from turtle import *

speed(0)

bgcolor("black")

colours = ["red", "purple", "blue", "green"]

for i in range(360):
  pencolor(colours[i % 2])
  width(i / 100 + 1)
  forward(i)
  left(89)
