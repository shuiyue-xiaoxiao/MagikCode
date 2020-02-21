# 1-9-4
# 画四格不同的正方形

from turtle import * # 从 turtle 库中导入全部函数

bgcolor("black") # 设置背景颜色：黑色

pensize(5) # 设置画笔粗细(5)

squareColor = ["red", "yellow", "orange", "blue", "green"] # 将颜色赋值给“正方形颜色”变量

up() # 抬起画笔

backward(200) # 往左200个像素

for color in squareColor: # 用 for 循环，编写四种不同颜色的循环，使用颜色列表作为变量
    pencolor(color) # 画笔依次选择一种颜色
    down() # 放下画笔
    for i in range(4): # 四条边/正方形循环
        forward(50) # 前进100个像素
        right(90) # 右转90度
    up() # 再次抬起画笔
    forward(100) # 前进100像素(为了区分开四个正方形)
ht() # 隐藏画笔
done() # 完成
