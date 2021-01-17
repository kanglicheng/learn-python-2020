class Scoop:
    def __init__(self, x):
        self.flavor = x


def create_scoops():
    flavors = ["vanilla", "chocolate", "strawberry"]
    res = []
    for x in flavors:
        y = Scoop(x)
        res.append(y)
    return res

# p = create_scoops()
# for x in p:
#     print(x.flavor)



class Animals:
    def __init__(self, species, color, number_of_legs = 4): # we can set default values for some of the attributes
        Animals.species = species
        Animals.color = color
        Animals.number_of_legs = number_of_legs
    
class Sheep(Animals):
    def __init__(self, species, color, number_of_legs):
        super().__init__(species, color, number_of_legs=number_of_legs)
    # we can add species-specific attributes here

# this is a simple example of object oriented program

s = Sheep("sheep", "white", "4")
print(s.species)
print(s.color)
print(s.number_of_legs)

