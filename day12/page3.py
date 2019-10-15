class Animal:

    def __init__(self):
        self._name = 'animal'

    def eat(self):
        print('I can eat any food')


# animal = Animal()
# animal.eat()


class Herbivourous(Animal):

    def __init__(self):
        super().__init__()

    def eat(self):
        print('I can eat only veg')


class Carnivourous(Animal):

    def __init__(self):
        super().__init__()

    def eat(self):
        print('I can eat meat')


h = Herbivourous()
h.eat() # I can eat only veg

c = Carnivourous()
c.eat() # I can eat meat
