"""
12.5 让球拍移动
"""

from tkinter import *
import time
import random

tk = Tk()
tk.title('paddle game')
tk.resizable(0, 0)  # 设置窗口的大小是否可以调整, (0, 0)的意思是在水平和垂直方向上都不能改变
tk.wm_attributes("-topmost", 1)  # 窗口置顶（无条件记住该方法和括号内的选项）

canvas = Canvas(tk, width=500, height=400, bd=0,
                highlightthickness=5)  # 指定高亮边框的宽度
canvas.pack()
tk.update()  # 刷新页面，为我们的游戏动画做好初始化


class Ball:
    def __init__(self, main_canvas, color):  # 创建 Ball 的类，它有两个参数：画布·main_canvas、球的颜色·color
        self.canvas = main_canvas  # 将参数 main_canvas 赋值给变量 canvas
        self.ID = main_canvas.create_oval(0, 0, 20, 20, fill=color)  # 在画布上画一个用颜色参数作为填充颜色的小球
        self.canvas.move(self.ID, 240, 190)  # 将tkinter画小球时所返回的ID保存起来

        start_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start_x)
        self.x = start_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.ID, self.x, self.y)
        pos = self.canvas.coords(self.ID)
        # print(pos)
        if pos[1] <= 0:
            self.y = 10
        if pos[3] >= self.canvas_height:
            self.y = -10

        if pos[0] <= 0:
            self.x = 10
        if pos[2] >= self.canvas_width:
            self.x = -10


class Paddle:
    def __init__(self, main_canvas, color):
        self.canvas = main_canvas
        self.ID = main_canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.ID, 200, 300)
        """step1: 增加对象变量 self.x"""
        self.x = 0
        """step2:调取画布的宽度赋值给 self.canvas_width"""
        self.canvas_width = self.canvas.winfo_width()
        """step4:将对应的按键的方向绑定在step3中生成的函数上"""
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        """pass"""
        """step5:修改 draw 的移动条件"""
        self.canvas.move(self.ID, self.x, 0)
        ball_pos = self.canvas.coords(self.ID)
        if ball_pos[0] <= 0:
            self.x = 0
        elif ball_pos[2] >= self.canvas_width:
            self.x = 0

        """step3: 创建两个函数来改变向左（turn_left）向右（turn_right）的方向"""

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3


paddle = Paddle(canvas, "LightSteelBlue")
ball = Ball(canvas, "Royalblue")


while True:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
