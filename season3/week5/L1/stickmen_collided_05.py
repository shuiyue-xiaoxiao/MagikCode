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
        for x in range(0, 10):
            for y in range(0, 8):
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


def overlap_x(co2, co1):
    if co2.x1 < co1.x1 < co2.x2 \
         or co2.x1 < co1.x2 < co2.x2 \
         or co1.x1 < co2.x1 < co1.x2 \
         or co1.x1 < co2.x2 < co1.x2:
        return True
    else:
        return False


def overlap_y(co1, co2):
    if co2.y1 < co1.y1 < co2.y2 \
            or co2.y1 < co1.y2 < co2.y2 \
            or co1.y1 < co2.y1 < co1.y2 \
            or co1.y1 < co2.y2 < co1.y2:
        return True
    else:
        return False


c1 = Coords(40, 40, 100, 100)  # (200, 200, 260, 260)
c2 = Coords(50, 50, 150, 150)  # (300, 300, 400, 400)
# print(overlap_x(co1, co2))
# print(overlap_y(co1, co2))

'''step4：对象冲突检测'''
'''判断左右前后是否相撞'''


def collided_left(co1, co2):
    if overlap_y(co1, co2):
        if co2.x1 < co1.x1 < co2.x2:
            return True
        return False


print(collided_left(c1, c2))


def collided_right(co1, co2):
    pass


def collided_top(co1, co2):
    pass


def collided_bottom(y, co1, co2):
    if overlap_x(co1, co2):
        y_clac = co1.y2 + y
        if co2.y1 < co1.y2 < co2.y2:
            return True
    return True


StickMen = Game()
mainloop()
