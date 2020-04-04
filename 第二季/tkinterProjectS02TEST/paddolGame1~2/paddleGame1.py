"""
12.1 让小球运动
"""

from tkinter import *
import time

"""step1: 窗口基本设置(创建基本游戏画布)"""

tk = Tk()
tk.title('paddle game')
tk.resizable(0, 0)  # 设置窗口的大小是否可以调整, (0, 0)的意思是在水平和垂直方向上都不能改变
tk.wm_attributes("-topmost", 1)  # 窗口置顶（无条件记住该方法和括号内的选项）

canvas = Canvas(tk, width=500, height=400, bd=0,
                highlightthickness=0)  # 指定高亮边框的宽度
canvas.pack()
tk.update()  # 刷新页面，为我们的游戏动画做好初始化

"""step2: 创建小球的 Ball 类"""


class Ball:
    def __init__(self, main_canvas, color):  # 创建 Ball 的类，它有两个参数：画布·main_canvas、球的颜色·color
        self.canvas = main_canvas  # 将参数 main_canvas 赋值给变量 canvas
        self.ID = main_canvas.create_oval(0, 0, 20, 20, fill=color)  # 在画布上画一个用颜色参数作为填充颜色的小球
        self.canvas.move(self.ID, 240, 190)  # 将tkinter画小球时所返回的ID保存起来

        """step5: 让小球运动"""

    def draw(self):
        self.canvas.move(self.ID, 0, +1)


"""step3: 创建一个小对象"""
ball = Ball(canvas, "Royalblue")

"""step4: 增加动画循环♻️"""

while True:
    """step6: 增加一个对小球对象 draw 函数的调用"""
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# 在关闭游戏窗口时，会出现错误信息 invalid command name ".!canvas"
# 这是因为关闭窗口时，draw() 还在运行，但 canvas 已经没有了
