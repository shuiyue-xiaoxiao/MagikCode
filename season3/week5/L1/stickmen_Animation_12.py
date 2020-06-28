from tkinter import *
from time import time, sleep

"""step1:创建 Game 类"""


class Game:

    def __init__(self):
        """创建 __init__ 函数（初始化）"""
        # '''设置窗口和画布'''
        # 创建一个 Tk 类的对象，并赋值给 self.tk 的变量
        self.tk = Tk()
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
        for y in range(0, 5):
            for x in range(0, 5):
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


# (200, 200, 260, 260)
c1 = Coords(40, 40, 100, 100)
# (300, 300, 400, 400)
c2 = Coords(50, 50, 150, 150)
print(overlap_x(c1, c2))
print(overlap_y(c1, c2))

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


'''step5：创建精灵类，'''


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinate = None

    # 之后要根据StickMan如何移动来编写代码
    def move(self):
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

        '''step9：绑定按键，变量设置'''
        '''变量设置'''
        # 对象变量 x 在运动时的水平方向（x1和x2）每次增加的量（不是坐标值）
        self.x = -2
        # 对象变量 y 在运动时的垂直方向（y1和y2）每次增加的量（不是坐标值）
        self.y = 0
        # 创建对象变量 current_image_index 来保存当前显示在屏幕上的图形的索引值
        # 设置当前索引值为 0
        self.current_image_index = 0
        # 下一个图形索引值的增量为 1
        self.current_image_index_add = 1
        # jump_cont(计数器)火柴人要用到它
        self.jump_count = 0
        # 调用 time 库中的 time() 函数，记录上一次火柴人移动的时间
        self.last_time = time()
        # 将对象变量设置成 Coords 类的对象，后面括号里没有参数是因为火柴人的数值会变
        self.coordinates = Coords()
        '''绑定按键'''
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    '''step10:创建左，右，跳函数'''
    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2

    def jump(self, evt):
        if self.y == 0:
            self.x = 2

    def turn_right(self, evt):
        # 火柴人在跳跃的过程中不能跳跃
        if self.y == 0:
            self.y = -4
            # 将计数器的值设为 0
            self.jump_count = 0

    '''step11:创建动画函数'''
    def animation(self):
        # 检查火柴人是否在水平方向上（向左或向右）移动
        # 如果在水平方向上并且没有跳跃，那么执行以下代码
        if self.x != 0 and self.y == 0:
            # 用于判断是否要画列表中的下一个图形
            # 用于当前时间减去变量 last_time 的值
            if time() - self.last_time > 0.1:
                # 相当于按下秒表重新计时
                self.last_time = time()
                # 递归公式
                # 生成当前图形的索引值
                self.current_image_index += self.current_image_index_add
                # 0 1 2 0 1 2 0 1 2 0 1 2……
                # 如果当前索引值大于等于 2
                if self.current_image_index >= 2:
                    # 图形递减
                    self.current_image_index_add = -1
                # 如果当前索引值小于等于 0
                if self.current_image_index <= 0:
                    # 图形递增
                    self.current_image_index_add = 1
        # 火柴人向左移动
        if self.x < 0:
            # 如果火柴人在向左跳跃中，加载图形 images_left[2]，否则在这个列表中循环
            # 火柴人跳跃中
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image_index])
        # 火柴人向右移动
        if self.x > 0:
            # 如果火柴人在向右跳跃中，加载图形 images_right[2]，否则在这个列表中循环
            # 火柴人跳跃中
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image_index])


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
