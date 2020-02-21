p = input('请输入国旗高度')  # 国旗尺寸
p = float(p)

a = 1.9  # 国旗一些重要数值
b = 1.0

c = 1.9*2/5
d = 7/13

e = c/12
f = d/10

k = 0.0616
l = 1/13
m = 0.37

import turtle as t   #相当于宏定义

t.setup(width=a*p, height=b*p)  # 设置画布大小
t.pencolor(0.698,0.132,0.203)  # 设置颜色1
t.fillcolor(0.698,0.132,0.203)  # 设置颜色2
t.speed(10)  # 设置画笔速度

for n1 in range(0,7):  # 画红色条纹
    t.penup()       #移动时不绘制图形,提起笔，用于另起一个地方绘制时用
    t.goto(-0.5*a*p,0.5*b*p-n1*2*l*p)  #移动位置
    t.begin_fill()       #准备开始填充图形
    for n2 in range(2):  
        t.forward(a*p)
        t.right(90)
        t.forward(l*p)
        t.right(90)
    t.end_fill()

t.penup()  # 画蓝色方块
t.goto(-0.5*a*p,0.5*b*p)
t.pencolor(0.234,0.233,0.430)
t.fillcolor(0.234,0.233,0.430)
t.begin_fill()
for n3 in range(2):
    t.forward(c*p)
    t.right(90)
    t.forward(d*p)
    t.right(90)
t.end_fill()

for i in range(1,10):  # 画星星
    if i%2 != 0:
        for j in range(1,7):
            t.penup()
            t.goto(-0.5*a*p+(2*j-1)*e*p,0.5*b*p-i*f*p+k*p/2)
            t.pencolor(1,1,1)
            t.fillcolor(1,1,1)
            t.begin_fill()
            t.right(90-18)
            t.forward(m*k*p)
            t.left(180-108)
            t.forward(m*k*p)
            for q in range(4):
                t.right(180-36)
                t.forward(m*k*p)
                t.left(180-108)
                t.forward(m*k*p)
            t.end_fill()
            t.right(90-18)
    else:
        for j in range(1,6):
            t.penup()
            t.goto(-0.5*a*p+2*j*e*p,0.5*b*p-i*f*p+k*p/2)   
            t.pencolor(1,1,1)
            t.fillcolor(1,1,1)
            t.begin_fill()
            t.right(90-18)
            t.forward(m*k*p)
            t.left(180-108)
            t.forward(m*k*p)
            for q in range(4):
                t.right(180-36)
                t.forward(m*k*p)
                t.left(180-108)
                t.forward(m*k*p)
            t.end_fill()
            t.right(90-18)

t.hideturtle()
p = input('请输入国旗高度')  # 国旗尺寸
p = float(p)

a = 1.9  # 国旗一些重要数值
b = 1.0

c = 1.9*2/5
d = 7/13

e = c/12
f = d/10

k = 0.0616
l = 1/13
m = 0.37

import turtle as t   #相当于宏定义

t.setup(width=a*p, height=b*p)  # 设置画布大小
t.pencolor(0.698,0.132,0.203)  # 设置颜色1
t.fillcolor(0.698,0.132,0.203)  # 设置颜色2
t.speed(10)  # 设置画笔速度

for n1 in range(0,7):  # 画红色条纹
    t.penup()       #移动时不绘制图形,提起笔，用于另起一个地方绘制时用
    t.goto(-0.5*a*p,0.5*b*p-n1*2*l*p)  #移动位置
    t.begin_fill()       #准备开始填充图形
    for n2 in range(2):  
        t.forward(a*p)
        t.right(90)
        t.forward(l*p)
        t.right(90)
    t.end_fill()

t.penup()  # 画蓝色方块
t.goto(-0.5*a*p,0.5*b*p)
t.pencolor(0.234,0.233,0.430)
t.fillcolor(0.234,0.233,0.430)
t.begin_fill()
for n3 in range(2):
    t.forward(c*p)
    t.right(90)
    t.forward(d*p)
    t.right(90)
t.end_fill()

for i in range(1,10):  # 画星星
    if i%2 != 0:
        for j in range(1,7):
            t.penup()
            t.goto(-0.5*a*p+(2*j-1)*e*p,0.5*b*p-i*f*p+k*p/2)
            t.pencolor(1,1,1)
            t.fillcolor(1,1,1)
            t.begin_fill()
            t.right(90-18)
            t.forward(m*k*p)
            t.left(180-108)
            t.forward(m*k*p)
            for q in range(4):
                t.right(180-36)
                t.forward(m*k*p)
                t.left(180-108)
                t.forward(m*k*p)
            t.end_fill()
            t.right(90-18)
    else:
        for j in range(1,6):
            t.penup()
            t.goto(-0.5*a*p+2*j*e*p,0.5*b*p-i*f*p+k*p/2)   
            t.pencolor(1,1,1)
            t.fillcolor(1,1,1)
            t.begin_fill()
            t.right(90-18)
            t.forward(m*k*p)
            t.left(180-108)
            t.forward(m*k*p)
            for q in range(4):
                t.right(180-36)
                t.forward(m*k*p)
                t.left(180-108)
                t.forward(m*k*p)
            t.end_fill()
            t.right(90-18)

t.hideturtle()
