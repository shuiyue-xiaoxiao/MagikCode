"""
step1:计划与准备
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>StickMan</title>
</head>
<body>
    <h1>Stick man escape game development plan</h1>
    <img src="stickman.png" alt="stickman" height="400" width="680">

    <h2>Game describe:</h2>
    <p>1:Little match man is trapped in a building. You have to help him out.</p>
    <p>2:In the game, there is a little match man, who can run from left to right, and he can jump.
        There are platforms on every floor, and he has to jump on them.</p>
    <p>3:He had to find the exit quickly, or the game was over.</p>
    <h2>stores reserve:</h2>

    <h3>1.Animated image of match man "running"</h3>
    <img src="gif/run_l3.gif" alt="run left 3" height="120" width="120">
    <img src="gif/run_l2.gif" alt="run left 2" height="120" width="120">
    <img src="gif/run_l1.gif" alt="run left 1" height="120" width="120">
    <img src="gif/run_r1.gif" alt="run right 1" height="120" width="120">
    <img src="gif/run_r2.gif" alt="run right 2" height="120" width="120">
    <img src="gif/run_r3.gif" alt="run right 3" height="120" width="120">

    <h3>2.A picture of the platform for the match man to "jump"</h3>
    <p>platform1:  30 x 10 <img src="gif/pf1.gif" alt="PlatFrom 1" height="10" width="30"></p>
    <p>platform2:  60 x 10 <img src="gif/pf2.gif" alt="PlatFrom 2" height="10" width="60"></p>
    <p>platform3: 100 x 10 <img src="gif/pf3.gif" alt="PlatFrom 3" height="10" width="100"></p>

    <h3>2.The door through which the match man can "escape"</h3>
    <p>Close 1: <img src="gif/door1.gif" alt="DoorClose 1" height="200" width="167"></p>
    <p>Open 2: <img src="gif/door2.gif" alt="DoorOpen 2" height="200" width="167"></p>

</body>
</html>
"""


from tkinter import *
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
        # self.tk.update()
        self.canvas_width = 1000
        self.canvas_height = 800


stickManGame = Game()

mainloop()
