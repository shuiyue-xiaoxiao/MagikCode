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

    def move(self):  # 之后要根据StickMan如何移动来编写代码
        pass

    def coords(self):
        return self.coordinate


'''step6:创建平台类'''


class PlatForm(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
        self.coordinate = Coords(x, y, x + width, y + height)


'''step7：创建门类'''


class Door(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
        self.coordinate = Coords(x, y, x + (width / 3), y + height)


'''step8：创建火柴人类'''


class StickMan(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
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
        self.image = game.canvas.create_image(40, 450, image=self.images_right[2], anchor="nw")


player = Game()

platform1 = PlatForm(player, PhotoImage(file="./gif/platform1.gif"), 30, 480, 100, 10)
platform2 = PlatForm(player, PhotoImage(file="./gif/platform1.gif"), 180, 440, 100, 10)
platform3 = PlatForm(player, PhotoImage(file="./gif/platform1.gif"), 330, 400, 100, 10)
platform4 = PlatForm(player, PhotoImage(file="./gif/platform2.gif"), 200, 350, 60, 10)
platform5 = PlatForm(player, PhotoImage(file="./gif/platform2.gif"), 80, 300, 60, 10)
platform6 = PlatForm(player, PhotoImage(file="./gif/platform2.gif"), 190, 220, 60, 10)
platform7 = PlatForm(player, PhotoImage(file="./gif/platform3.gif"), 330, 160, 30, 10)
platform8 = PlatForm(player, PhotoImage(file="./gif/platform3.gif"), 200, 120, 30, 10)
platform9 = PlatForm(player, PhotoImage(file="./gif/platform2.gif"), 100, 70, 60, 10)
player.sprites.append(platform1)
player.sprites.append(platform2)
player.sprites.append(platform3)
player.sprites.append(platform4)
player.sprites.append(platform5)
player.sprites.append(platform6)
player.sprites.append(platform7)
player.sprites.append(platform8)
player.sprites.append(platform9)

door = Door(player, PhotoImage(file="./gif/door1.gif"), 115, 33, 40, 35)
player.sprites.append(door)

sm = StickMan(player)
player.sprites.append(sm)


mainloop()
