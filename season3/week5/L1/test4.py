from tkinter import *
from time import sleep

"""step1:创建 Game 类"""


class Game:
    def __init__(self):  # 创建 __init__ 函数（初始化）
        # 设置窗口和画布
        self.tk = Tk()  # 创建一个 Tk 类的对象，并赋值给 self.tk 的变量
        self.tk.title('火柴人逃生游戏')
        # self.tk.resizable(0, 0)
        self.tk.wm_attributes('-topmost', 0)
        self.tk.canvas = Canvas(self.tk, width=500, height=500,
                                highlightthickness=0)
        self.tk.canvas.pack()
        self.tk.update()
        self.canvas_width = 500
        self.canvas_height = 500
        """继续完成 __init__ 函数"""
        self.background = PhotoImage(file="./gif/bg500.gif")
        width = self.background.width()
        height = self.background.height()
        self.tk.canvas.create_image(width, height,
                                    image=self.background,
                                    anchor='se')

        self.sprites = []
        self.running = True

    '''step2：创建主循环函数'''

    def mainloop(self):
        while True:
            if self.running:
                for sprite in self.sprites:
                    sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                sleep(1)


StickMen = Game()
mainloop()
