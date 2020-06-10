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
        self.canvas = Canvas(self.tk, width=500, height=500,
                             highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_width = 500
        self.canvas_height = 500
        """继续完成 __init__ 函数"""
        self.background = PhotoImage(file="./gif/bg100.gif")
        width = self.background.width()
        height = self.background.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * width, y * height,
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


def collided_right(co1, co2):
    if overlap_y(co1, co2):
        if co2.x1 < co1.x1 < co2.x2:
            return True
        return False


def collided_top(co1, co2):
    if overlap_x(co1, co2):
        if co2.y1 < co1.y1 < co2.y2:
            return True
        return False


def collided_bottom(y, co1, co2):
    if overlap_x(co1, co2):
        y_clac = co1.y2 + y
        if co2.y1 < co1.y2 < co2.y2:
            return True
    return True


'''step5：创建精灵类'''


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinate = None

    def move(self):
        pass

    def coords(self):
        return self.coordinate


class PlatForm(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
        self.coordinate = Coords(x, y, x + width, y + height)


StickMen = Game()
platform1 = PlatForm(StickMen, PhotoImage(file="./gif/platform1.gif"), 30, 480, 100, 10)
platform2 = PlatForm(StickMen, PhotoImage(file="./gif/platform1.gif"), 180, 440, 100, 10)
platform3 = PlatForm(StickMen, PhotoImage(file="./gif/platform1.gif"), 330, 400, 100, 10)
platform4 = PlatForm(StickMen, PhotoImage(file="./gif/platform2.gif"), 200, 350, 60, 10)
platform5 = PlatForm(StickMen, PhotoImage(file="./gif/platform2.gif"), 80, 300, 60, 10)
platform6 = PlatForm(StickMen, PhotoImage(file="./gif/platform2.gif"), 190, 220, 60, 10)
platform7 = PlatForm(StickMen, PhotoImage(file="./gif/platform3.gif"), 330, 160, 30, 10)
platform8 = PlatForm(StickMen, PhotoImage(file="./gif/platform3.gif"), 200, 120, 30, 10)
platform9 = PlatForm(StickMen, PhotoImage(file="./gif/platform2.gif"), 100, 70, 60, 10)
StickMen.sprites.append(platform1)
StickMen.sprites.append(platform2)
StickMen.sprites.append(platform3)
StickMen.sprites.append(platform4)
StickMen.sprites.append(platform5)
StickMen.sprites.append(platform6)
StickMen.sprites.append(platform7)
StickMen.sprites.append(platform8)
StickMen.sprites.append(platform9)
mainloop()
