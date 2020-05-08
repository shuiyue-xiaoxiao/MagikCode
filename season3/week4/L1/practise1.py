class Animals:
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
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def Eat_bamboos(self):
        pass


class Mankind(Mammals):
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def bipedalism(self):
        pass


Alice = Pandas()
Alice.set_name(name=input('Please title your panda: \n'))

Jason = Mankind()
Jason.set_name(name=input('Please title your name: \n'))

print(Alice.name + ': hello ' + Jason.name)

