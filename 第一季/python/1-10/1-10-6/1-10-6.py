# 1-10-6_Tai_Ji
# 阴阳太极图
 
from turtle import *
import time
 
setup(600, 600)
 
def coordinate_system(): # 建立坐标系函数
    speed(0) 
    dot(10, "red") 
    pencolor("LightGrey") 
      
    row_y = 300
    for i in range(int(600 / 20 - 1)): 
        row_y -= 20
        up()
        goto(-300, row_y)
        down()
        fd(600)
 
    right(90)
        
    column_x = -300
    for i in range(int(600 / 20 - 1)): 
        column_x += 20
        up()
        goto(column_x, 300)
        down()
        fd(600)
 
# ————————画笔回到初始位置———————— #
 
    up()
    home() # 回到初始位置(坐标和方向)
    down()
 
# ————————调用坐标系函数———————— #
 
coordinate_system()
 
# -----------以下开始绘画-----------
 
# 基本设置
up()
goto(0, -200)
pencolor("black")
speed(5)
down()
 
# 一个完整的圆,分两次画
fillcolor("white")
begin_fill()
circle(200, 180)
end_fill()
 
fillcolor("black")
begin_fill()
circle(200, 180)
end_fill()
 
# 下面的半圆
fillcolor("white")
begin_fill()
circle(100, -180)
end_fill()
 
# 上面的半圆
fillcolor("black")
begin_fill()
circle(-100, -180)
end_fill()
 
# 上面的小圆
up()
goto(0, 80)
down()
fillcolor("white")
begin_fill()
circle(20)
end_fill()
 
# 下面的小圆
up()
goto(0, -120)
down()
fillcolor("black")
begin_fill()
circle(20)
end_fill()
 
ht()
done()
