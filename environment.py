import random


class environment:
    def __init__(self):
        self.size = 10
        self.grid = grid_create()

    def grid_create(self):
        grid = []
        x = 0
        y = 0
        xrow = []
        while x < self.size:
            xrow[y] = location(x, y)


    def main(self, organisms):
        # Anything in environment that needs to change (e.g. plants grow)

        # Environment acts on organisms
        return


    def live(self, organisms):
        for num in range(len(organisms.organisms)):
            organism = organisms.organisms[num]
            organism.health += self.food
            self.food -= 1
# test
grid = []
counter1=0
counter2=0
xrow=[]
while counter1 < 20:
    xrow[counter2] = location(counter1, counter2)
    counter2 += 1
    if counter2 > 20:
        counter2 = 0
        counter1 += 1
        grid.append(xrow)
        xrow=[]
print(grid)

class location():
    """A location object to include position characteristics"""
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.temperature = 0  # between -20 and 40
        self.plant_food = 0  # units of food for herbivores
        self.meat_food = 0  # units of food for carnivores
        self.terrain = 'grass'  # terrain type (from a list somewhere)
        self.humidity = 0  # water content (between 0 and 1)
        self.light_level = 0  # how bright a place is (between 0 and 1)

    def randomise(self):
        self.temperature = random.randint(-20, 40)
        self.plant_food = random.randint(0, 1000)
        self.meat_food = random.randint(0, 200)
        self.humidity = random.random
        self.light_level = random.random

    def plants_grow(self):
        self.plant_food = (1 + self.light_level) * self.plant_food

    def meat_rots(self):
        self.meat_food -= (self.humidity * max(0, self.temperature) / 40) * self.meat_food

