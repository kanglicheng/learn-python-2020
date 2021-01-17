# 1 ice cream
from typing import AsyncIterable


class scoop:
    def __init__(self, strinput):
        self.flavor = strinput


def threeicecream():
    output = []
    flavors = ["strawberry", "mint chocolate", "almond"]
    for i in flavors:
        x = scoop(i)
        output.append(x)
    return output


y = threeicecream()
for i in y:
    print(i.flavor)

# animals


class animal:
    def __init__(self, inputcolor, inputspecies, inputlegs):
        self.color = inputcolor
        self.species = inputspecies
        self.number_of_legs = inputlegs


class sheep(animal):
    def __init__(self, inputcolor, inputspecies, inputlegs=4):
        super().__init__(inputcolor, inputspecies, inputlegs)


class wolf(animal):
    def __init__(self, inputcolor, inputspecies, inputlegs=4):
        super().__init__(inputcolor, inputspecies, inputlegs)


class snake(animal):
    def __init__(self, inputcolor, inputspecies, inputlegs=0):
        super().__init__(inputcolor, inputspecies, inputlegs)


class parrot(animal):
    def __init__(self, inputcolor, inputspecies, inputlegs=2):
        super().__init__(inputcolor, inputspecies, inputlegs)
