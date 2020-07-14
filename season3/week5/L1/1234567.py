from tkinter import *
import time
"""step1:创建 Game 类"""


class Game:
    def __init__(self):  # 创建 __init__ 函数（初始化）
        # 设置窗口和画布
        self.tk = Tk()  # 创建一个 Tk 类的对象，并赋值给 self.tk 的变量
        self.tk.title('火柴人逃生游戏')
        self.tk.resizable(0, -1)
        self.tk.wm_attributes('-topmost', 0)
        self.tk.canvas = Canvas(self.tk, width=500, height=500,
                                highlightthickness=0)
        self.tk.canvas.pack()
        self.images_left = [
            PhotoImage(file='./gif/run_l1.gif'),
            PhotoImage(file='./gif/run_l2.gif'),
            PhotoImage(file='./gif/run_l3.gif')
        ]
        self.images_right = [
            PhotoImage(file='./gif/run_r1.gif'),
            PhotoImage(file='./gif/run_r2.gif'),
            PhotoImage(file='./gif/run_r3.gif')
        ]
        self.image = self.tk.canvas.create_image(250, 250, image=self.images_left[2], anchor="nw")
        self.current_image_index = 0
        # 下一个图形索引值的增量为 1
        self.current_image_index_add = 1


stickManGame = Game()

for i in range(100):
    stickManGame.current_image_index += stickManGame.current_image_index_add
    # 0 1 2 0 1 2 0 1 2 0 1 2……
    # 如果当前索引值大于等于 2
    if stickManGame.current_image_index >= 2:
        # 图形递减
        stickManGame.current_image_index_add = -1
    # 如果当前索引值小于等于 0
    if stickManGame.current_image_index <= 0:
        # 图形递增
        stickManGame.current_image_index_add = 1
    stickManGame.tk.canvas.itemconfig(stickManGame.image, image=stickManGame.images_left[stickManGame.current_image_index])
    stickManGame.tk.update()
    time.sleep(0.2)

mainloop()
