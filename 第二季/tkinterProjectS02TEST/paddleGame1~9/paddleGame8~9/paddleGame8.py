from tkinter import *


class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def delete(self):
        self.canvas.delete(self.item)

    def get_coords(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)


class Racket(GameObject):
    def __init__(self, canvas, x, y):
        item = canvas.create_rectangle(x, y, x + 100, y + 10, fill='green')
        super().__init__(canvas, item)

    def draw(self, offset):
        pos = self.get_coords()
        width = self.canvas.winfo_width()
        if pos[0] + offset >= 0 and pos[2] + offset <= width:
            super().move(offset, 0)


class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.direction = [1, -1]
        self.speed = 15
        item = canvas.create_oval(x, y, x + 20, y + 20, fill='blue')
        super().__init__(canvas, item)

    def draw(self):
        pos = self.get_coords()
        self.canvas_width = self.canvas.winfo_width()
        if pos[1] <= 0:
            self.direction[1] *= -1
        if game.hit_racket():
            self.direction[1] *= -1
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.direction[0] *= -1
        # 偏移量
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)


class Game(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lives = 3
        self.scores = 0
        self.width = 800
        self.height = 600

        self.canvas = Canvas(self, bg='#F8C26C', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()

        self.ball = None
        self.lives_text = None
        self.scores_text = None

        self.racket = Racket(self.canvas, self.width / 2 - 50, 480)

        self.setup_game()
        self.canvas.focus_set()

        self.canvas.bind('<KeyPress-Left>', lambda turn_left: self.racket.draw(-40))
        self.canvas.bind('<KeyPress-Right>', lambda turn_right: self.racket.draw(40))

    def setup_game(self):
        self.reset_ball()

        self.update_lives_text()
        self.update_scores_text()
        self.text = self.canvas.create_text(400, 200, text='单击鼠标左键开始游戏', font=('Helvetica', 36))
        self.canvas.bind('<Button-1>', lambda start_game: self.start_game())

    def reset_ball(self):
        if self.ball is not None:
            self.ball.delete()
        racket_pos = self.racket.get_coords()
        x = (racket_pos[0] + racket_pos[2]) * 0.5 - 10
        self.ball = Ball(self.canvas, x, 350)

    def update_lives_text(self):
        text = '生命: %s' % self.lives
        if self.lives_text is None:
            self.lives_text = self.canvas.create_text(60, 30, text=text, font=('Helvetica', 16), fill='green')
        else:
            self.canvas.itemconfig(self.lives_text, text=text)

    def update_scores_text(self):
        text = '得分: %s' % self.scores
        if self.scores_text is None:
            self.scores_text = self.canvas.create_text(60, 60, text=text, font=('Helvetica', 16), fill='green')
        else:
            self.scores = self.scores + 1
            text = '得分: %s' % self.scores
            self.canvas.itemconfig(self.scores_text, text=text)

    def start_game(self):
        self.canvas.unbind('<Button-1>')
        self.reset_score()
        self.canvas.delete(self.text)
        self.game_loop()

    def reset_score(self):
        self.scores = 0
        text = '得分: %s' % self.scores
        self.canvas.itemconfig(self.scores_text, text=text)

    def game_loop(self):
        if self.ball.get_coords()[3] >= self.height:
            self.ball.speed = 0
            self.lives -= 1
            if self.lives < 0:
                self.canvas.create_text(400, 200, text='游戏结束', font=('Helvetica', 36), fill='red')
            else:
                self.scores = self.scores - 1
                self.after(1000, self.setup_game)
        else:
            self.ball.draw()
            self.after(50, self.game_loop)

    def hit_racket(self):
        ball_pos = self.ball.get_coords()
        racket_pos = self.racket.get_coords()
        if ball_pos[2] >= racket_pos[0] and ball_pos[0] <= racket_pos[2]:
            if racket_pos[1] <= ball_pos[3] <= racket_pos[3]:
                self.update_scores_text()
                return True
        return False


if __name__ == '__main__':
    window = Tk()
    window.title('弹球游戏')
    # 设定窗口大小不可改变
    window.resizable(0, 0)
    # 设定窗口总是显示在最前面
    window.wm_attributes("-topmost", 1)
    game = Game(window)
    game.mainloop()
