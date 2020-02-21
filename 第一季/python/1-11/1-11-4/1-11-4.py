# 1-11-4_Doraemon
# 哆啦A梦_程序解析4
 
'''
凯戈老师的编程大师课，关注魔力小孩官方微信号。
www.magikidlab.com
'''
 
from turtle import *
 
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
 
# coordinate_system()
 
# -----------以下开始绘画-----------
 
# 无痕移动画笔
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()
 
# 眼睛
def eyes():
    fillcolor("#ffffff")
    begin_fill()
 
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()
 
 
# 胡须
def beard():
    my_goto(-32, 135)
    seth(165)
    fd(60)
 
    my_goto(-32, 125)
    seth(180)
    fd(60)
 
    my_goto(-32, 115)
    seth(193)
    fd(60)
 
    my_goto(37, 135)
    seth(15)
    fd(60)
 
    my_goto(37, 125)
    seth(0)
    fd(60)
 
    my_goto(37, 115)
    seth(-13)
    fd(60)
 
# 嘴巴
def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)
 
# 红色围脖
def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0) # 设置画笔的方向
    fd(200)
    circle(-5, 90) # 画圆角的技巧
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()
 
# 鼻子
def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()
 
# 黑眼睛
def black_eyes():
    seth(0)
    my_goto(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()
 
    pensize(6)
    my_goto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)
 
    my_goto(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    my_goto(0, 0)
 
  
 
# 脸
def face():
 
    fd(180)
    lt(45) # 画笔左转45度，开始画脸部轮廓。
    fillcolor('#ffffff')
    begin_fill()
    pencolor("red") # 为了看得更清楚脸部轮廓的起始位置，和 lt(45) 对照来看
    circle(120, 100)

    seth(180) # seth(setheading)，设置画笔方向从右到左(从左到右是0度)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    my_goto(63.56,218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)
    
# 头型
def head():
    penup()
    circle(150, 40) # 起始笔不放下
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280) # 笔放下以后，左边也是对称的40，360减去2个40，就等于280.
    end_fill()
#    penup()
#    circle(150, 20)
#    pendown()
     
# ————————以上是定义函数，以下是调用函数绘画———————— #
 
# 画哆啦A梦
def Doraemon():
    # 头型
    head()
 
    # 红色围脖
    scarf()
 
    # 脸
    face()
'''
    # 红鼻子
    nose()
 
    # 嘴巴
    mouth()
 
    # 胡须
    beard()
 
    # 身体
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)
 
 
    fillcolor('#00a0de')
    begin_fill()
 
    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)
 
    # print(pos())
 
    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)
 
    # print(pos())
    seth(100)
    circle(-1000, 9)
 
    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)
 
    # print(pos())
 
 
    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()
 
    # 左手
    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()
 
    # 脚
    my_goto(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()
 
    my_goto(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()
 
    # 右手
    my_goto(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()
 
    # 口袋
    my_goto(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()
 
    my_goto(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)
 
    #铃铛
    my_goto(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180-10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    my_goto(0, -150)
 
    # 画眼睛
    black_eyes()
'''
if __name__ == '__main__':
    screensize(800,600, "#f0f0f0")
    pencolor("LightGrey")
    pensize(3)  # 画笔宽度
    speed(3)    # 画笔速度
    Doraemon()
    my_goto(100, -300)
    write('Magikidlab.com', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()
