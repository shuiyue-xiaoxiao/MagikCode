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
        self.tk.canvas = Canvas(self.tk, width=500, height=500,
                                highlightthickness=0)
        self.tk.canvas.pack()
        self.tk.update()
        self.canvas_width = 500
        self.canvas_height = 500
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


def overlap_x(co2, co1):
    """判断两个对象在水平方向上是否有重叠"""
    if co2.x1 < co1.x1 < co2.x2 \
            or co2.x1 < co1.x2 < co2.x2 \
            or co1.x1 < co2.x1 < co1.x2 \
            or co1.x1 < co2.x2 < co1.x2:
        return True
    else:
        return False


def overlap_y(co1, co2):
    if co2.y1 < co1.y1 < co2.y2:
        return True
    elif co2.y1 < co1.y2 < co2.y2:
        return True
    elif co1.y1 < co2.y1 < co1.y2:
        return True
    elif co1.y1 < co2.y2 < co1.y2:
        return True
    else:
        return False


coords1 = Coords(40, 40, 100, 100)  # (200, 200, 260, 260)
coords2 = Coords(300, 300, 400, 400)  # (50, 50, 150, 150)
print(overlap_x(coords1, coords2))
print(overlap_y(coords1, coords2))


StickMen = Game()
mainloop()
