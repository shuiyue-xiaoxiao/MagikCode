from turtle import *

colors = ["yellow", "green", "blue", "red"]
size = 1
for i in range(1, 360):
    pencolor(i % 4)
    forward(size)
    right(91)
    size = size + 1
