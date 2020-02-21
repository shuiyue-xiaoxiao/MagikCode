# 1-10-2 圆 组 成 的 漂 亮 图 形

# 画圆(最简单的)

from turtle import *

speed(0)

circle(50)
circle(100)
circle(150)

circle(-50)
circle(-100)
circle(-150)

left(90)

circle(50)
circle(100)
circle(150)

circle(-50)
circle(-100)
circle(-150)

left(45)

circle(50)
circle(100)
circle(150)

circle(-50)
circle(-100)
circle(-150)

left(90)

circle(50)
circle(100)
circle(150)

circle(-50)
circle(-100)
circle(-150)

ht()
done()

'''
公式：turtle.circle(radius, extent = None, steps = None)

绘制一个 radius 指定半径的圆。
圆心在海龟左边 radius 个单位;

extent 为一个夹角，用来决定绘制圆的一部分
如未指定 extent *则绘制整个圆
如* extent不是完整圆周，则以当前画笔位置为一个端点绘制圆弧

如果 radius 为正值则朝逆时针方向绘制圆弧，否则朝顺时针方向。
最终海龟的朝向会依据 extent 的值而改变。
'''


