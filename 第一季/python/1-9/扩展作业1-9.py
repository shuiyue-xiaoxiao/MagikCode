from turtle import *

x = 0
y = 0
long = 50
color = ["red", "yellow", "orange", "blue"]
speed(0)

for i in range(40):
    for i in color:
        pencolor(i)
        forward(long)
        right(90)
    x = x - 5
    setx(x)    
    y = y + 5
    sety(y = y + 1)
    long = long + 10
