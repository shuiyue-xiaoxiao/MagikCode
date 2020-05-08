class Things:
    pass


class Inanimate(Things):
    pass


class Animate(Things):
    pass


class Boxes(Inanimate):
    pass


class Animals(Animate):
    def Breathe(self):
        pass

    def Move(self):
        pass

    def Eat_food(self):
        pass


class Mammals(Animals):
    def Feed_milk(self):
        pass


class Pandas(Mammals):
    def Eat_bamboos(self):
        pass


Alice = Pandas()
Alice.Move()
Alice.Eat_bamboos()

Jason = Pandas()
Jason.Move()

