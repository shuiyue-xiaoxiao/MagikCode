"""
12.6 判断小球是否被球拍击中
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
    """修改 __init__ 参数"""
    """step1:添加 paddle 参数"""
    def __init__(self, main_canvas, paddle, color):  # 创建 Ball 的类，它有两个参数：画布·main_canvas、球的颜色·color
        self.canvas = main_canvas  # 将参数 main_canvas 赋值给变量 canvas
        """step2：将球拍参数 paddle 赋值给变量 paddle"""
        self.paddle = paddle
        self.ID = main_canvas.create_oval(0, 0, 20, 20, fill=color)  # 在画布上画一个用颜色参数作为填充颜色的小球
        self.canvas.move(self.ID, 240, 190)  # 将tkinter画小球时所返回的ID保存起来

        start_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start_x)
        self.x = start_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        """step5:创建函数 hit_paddle"""

    def hit_paddle(self, ball_pos):
        paddle_pos = self.canvas.coords(self.paddle.ID)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= ball_pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.ID, self.x, self.y)
        pos = self.canvas.coords(self.ID)
        # print(pos)
        if pos[1] <= 0:
            self.y = 10
        if pos[3] >= self.canvas_height:
            self.y = -10
        """step4:添加小球击中球拍的函数 hit_paddle"""
        if self.hit_paddle(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 10
        if pos[2] >= self.canvas_width:
            self.x = -10


class Paddle:
    def __init__(self, main_canvas, color):
        self.canvas = main_canvas
        self.ID = main_canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.ID, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        """pass"""
        self.canvas.move(self.ID, self.x, 0)
        ball_pos = self.canvas.coords(self.ID)
        if ball_pos[0] <= 0:
            self.x = 0
        elif ball_pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3


paddle = Paddle(canvas, "LightSteelBlue")
"""step3: 在ball的变量中，加上paddle参数"""
ball = Ball(canvas, paddle, "Royalblue")


while True:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
