class Things(object):
    pass


class Inanimate(Things):
    pass


class Animate(Things):
    pass


class Boxes(Inanimate):
    pass


class PaperBoxes(Boxes):
    pass


class PlasticBoxes(Boxes):
    pass


class botany(Animate):
    def photosynthesis(self):
        pass


class Animals(Animate):
    def Breathe(self):
        pass

    def Move(self):
        pass

    def Eat_food(self):
        pass


class Bird(Animals):
    def ley_eggs(self):
        pass


class Hummingbird(Bird):
    def __init__(self):
        print('I\'m the smallest bird in the world')


class Reptile(Animals):
    def ley_eggs(self):
        pass


class Snake(Reptile):
    def __init__(self):
        print('I don\'t have legs')


class Mammals(Animals):
    def Feed_milk(self):
        pass


class Pandas(Mammals):
    def Eat_bamboos(self):
        pass


Jason = Hummingbird()
print(Jason)

Alice = Snake()
print(Alice)
