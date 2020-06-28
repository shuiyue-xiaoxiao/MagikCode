from tkinter import *
from time import sleep

"""step1:创建 Game 类"""


class Game:
    def __init__(self):  # 创建 __init__ 函数（初始化）
        # 设置窗口和画布
        self.tk = Tk()  # 创建一个 Tk 类的对象，并赋值给 self.tk 的变量
        self.tk.title('火柴人逃生游戏')
        self.tk.resizable(0, 0)
        self.tk.wm_attributes('-topmost', 0)
        self.tk.canvas = Canvas(self.tk, width=1000, height=800,
                                highlightthickness=0)
        self.tk.canvas.pack()
        self.tk.update()
        self.canvas_width = 1000
        self.canvas_height = 800
        """继续完成 __init__ 函数"""
        self.background = PhotoImage(file="./gif/bg100.gif")
        width = self.background.width()
        height = self.background.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.tk.canvas.create_image(x * width, y * height,
                                            image=self.background,
                                            anchor='nw')

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
                sleep(0.01)


'''step3：创建坐标类'''


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def overlap_x(platform, stickman):
    if platform.x1 < stickman.x1 < platform.x2 \
         or platform.x1 < stickman.x2 < platform.x2 \
         or stickman.x1 < platform.x1 < stickman.x2 \
         or stickman.x1 < platform.x2 < stickman.x2:
        return True
    else:
        return False


def overlap_y(stickman, platform):
    if platform.y1 < stickman.y1 < platform.y2 \
            or platform.y1 < stickman.y2 < platform.y2 \
            or stickman.y1 < platform.y1 < stickman.y2 \
            or stickman.y1 < platform.y2 < stickman.y2:
        return True
    else:
        return False


stickman1 = Coords(40, 40, 100, 100)  # (200, 200, 260, 260)
platform1 = Coords(50, 50, 150, 150)  # (300, 300, 400, 400)
# print(overlap_x(stickman1, platform1))
# print(overlap_y(stickman1, platform1))

'''step4：对象冲突检测'''
'''判断左右前后是否相撞'''


def collided_left(stickman, platform):
    if overlap_y(stickman, platform) \
            and platform.x1 < stickman.x1 < platform.x2:
        return True
    return False


def collided_right(stickman, platform):
    if overlap_y(stickman, platform):
        if platform.x1 < stickman.x1 < platform.x2:
            return True
        return False


def collided_top(stickman, platform):
    if overlap_x(stickman, platform):
        if platform.y1 < stickman.y1 < platform.y2:
            return True
        return False


def collided_bottom(y, stickman, platform):
    if overlap_x(stickman, platform):
        y_clac = stickman.y2 + y
        if platform.y1 < stickman.y2 < platform.y2:
            return True
    return False


StickMen = Game()
mainloop()
