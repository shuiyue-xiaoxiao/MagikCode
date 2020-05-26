from tkinter import *

'''step1 创建 Game 类'''


class Game:
    def __init__(self):  # 创建一个 __init__ 函数，用于初始化
        # 创建一个属于 tkinter 类的窗口
        self.tk = Tk()
        self.tk.title('火柴人逃生游戏')
        self.tk.resizable(0, 0)
        self.tk.wm_attributes('-topmost', 1)
        self.tk.canvas = Canvas(self.tk, width=500, height=500,
                                highlightthickness=0)
        self.tk.canvas.pack()
        self.tk.update()
        self.canvas_width = 500
        self.canvas_height = 500


stickMen = Game()
mainloop()
