# 1-9-3 Assign a list to a variable
# 列表和循环：将列表赋值给变量

from turtle import *

'''
# 试着将列表中的数据项改成任意不同数据类型的元素
# 运行后再查看结果
for i in [1, 'transportation', 3.5, True]:
    forward(100)
    right(90)


# 提示：可将列表[1， 2， 3， 4]赋值给一个变量，比如
list1 = [1, 2, 3, 4]

# 上面程序可写成：
for i in list1:
    forward(100)
    right(90)
'''
# 用四种不同颜色画出四条边
# 将颜色列表赋值给颜色变量


sideColor = ["red", "green", "orange", "blue"]

for color in sideColor:
    pencolor(color)
    forward(100)
    right(90)

# 如果看的不清楚，可以将画笔加粗，或者设置背景颜色, 或者停顿时间。
bgcolor("black")
pensize(50)

for color in sideColor:
    pencolor(color)
    forward(100)
    right(90)
