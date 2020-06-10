from turtle import *
import time

bgcolor("#08203D")
shape("turtle")
turtlesize(2, 2, 2)

up()
goto(0, -200)
down()
color = ["yellow", "green", "#FF1493", "#C71585", "orange", "#9400D3",
         "#7B68EE", "#483D8B", "#E6E6FA", "#0000FF", "#40E0D0", "#B0E0E6", "#FF7F50", "#A0522D"]

time.sleep(1)
speed(0)
pencolor("red")
pensize(3)
circle(200)
hideturtle()

time.sleep(1)
clear()

for i in range(len(color)):
    speed(0)
    pencolor(color[i])
    pensize(3)
    circle(200, None, i + 3)
    hideturtle()
    time.sleep(1)
    clear()

mainloop()


