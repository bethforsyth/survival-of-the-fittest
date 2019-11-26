import random
import math



class environment:
    """The environment objects"""
    def grid_create(self):
        grid = []
        x = 0
        y = 0
        xrow = []
        while x < self.size:
            xrow.append(location(x, y))
            xrow[y].randomise()
            y += 1
            if y >= self.size:
                y = 0
                x += 1
                grid.append(xrow)
                xrow = []
        return grid

    def __init__(self):
        self.size = 10
        self.grid = self.grid_create()
        self.standard_environment()

    def main(self, organisms):
        # Anything in environment that needs to change (e.g. plants grow)

        # Environment acts on organisms
        return

    def live(self, organisms):
        for num in range(len(organisms.organisms)):
            organism = organisms.organisms[num]
            organism.health += self.food
            self.food -= 1

    def standard_environment(self):
        for i in range(self.size):
            humidity = i / self.size
            for j in range(self.size):
                temperature = -20 + 60 * j / self.size
                self.grid[i][j].humidity = humidity
                self.grid[i][j].temperature = temperature

    def location(self, pos):
        return self.grid[pos[0]][pos[1]]

    def list_locations(self):
        locations = []
        for row in self.grid:
            for location in row:
                locations.append(location)
        return locations

    def grow_plants(self):
        locations = self.list_locations()
        for location in locations:
            location.plants_grow()

    def count_organisms(self, organisms):
        locations = self.list_locations()
        for location in locations:
            location.organism_count(organisms)


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
        self.organism_number = 0
        self.organisms_list = []

    def randomise(self):
        self.temperature = random.randint(-20, 40)
        self.plant_food = random.randint(0, 30)
        self.meat_food = random.randint(0, 200)
        self.humidity = random.random()
        self.light_level = random.random()

    def plants_grow(self):
        self.plant_food = math.floor((1 + 0.25 * self.light_level) * self.plant_food)

    def meat_rots(self):
        self.meat_food -= (self.humidity * max(0, self.temperature) / 40) * self.meat_food

    def organism_count(self, organisms):
        self.organism_number = 0
        self.checked_location = (self.xpos, self.ypos)
        for creature in organisms.organisms:
            if creature.current_pos == self.checked_location:
                self.organism_number += 1
            else:
                pass