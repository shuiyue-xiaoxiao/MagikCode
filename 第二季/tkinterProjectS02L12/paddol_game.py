

# 游戏对象的一些通用方法：
class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def delete(self):
        self.canvas.delete(self.item)

    def get_coords(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.itim, x, y)


class Racket(GameObject):
    def __init__(self, canvas, x, y):
        item = canvas.crate_rectangle(x, y, x + 100, y + 10, fill='green')
        super. __init__(canvas, item)

    def draw(self, offset):
        pos = self.get_coords()
        width = self.canvas.winfo_width()

