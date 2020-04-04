"""
12.2 让小球来回反弹
"""

from tkinter import *
import time

tk = Tk()
tk.title('paddle game')
tk.resizable(0, 0)  # 设置窗口的大小是否可以调整, (0, 0)的意思是在水平和垂直方向上都不能改变
tk.wm_attributes("-topmost", 1)  # 窗口置顶（无条件记住该方法和括号内的选项）

canvas = Canvas(tk, width=500, height=400, bd=0,
                highlightthickness=0)  # 指定高亮边框的宽度
canvas.pack()
tk.update()  # 刷新页面，为我们的游戏动画做好初始化


class Ball:
    def __init__(self, main_canvas, color):  # 创建 Ball 的类，它有两个参数：画布·main_canvas、球的颜色·color
        self.canvas = main_canvas  # 将参数 main_canvas 赋值给变量 canvas
        self.ID = main_canvas.create_oval(0, 0, 20, 20, fill=color)  # 在画布上画一个用颜色参数作为填充颜色的小球
        self.canvas.move(self.ID, 240, 190)  # 将tkinter画小球时所返回的ID保存起来

        """step1: 在小球 Ball 类初始化函数里，再加上几个对象变量"""

        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()

        """step2:再次修改 draw 函数"""

    def draw(self):
        self.canvas.move(self.ID, self.x, self.y)
        pos = self.canvas.coords(self.ID)
        # print(pos)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1


"""step3: 创建一个小对象"""
ball = Ball(canvas, "Royalblue")

"""step4: 增加动画循环♻️"""

while True:
    """step6: 增加一个对小球对象 draw 函数的调用"""
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
