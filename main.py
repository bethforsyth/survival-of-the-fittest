import logging

class organism:
    def __init__(self):
        self.code = "0001011010101"
        self.size = 10
        self.health = 5

    def death(self):
        if self.health < 4:
            return true

    def reproduce(self):
        if self.health > 6:
            return true

class environment:

    def __init__(self):
        self.food = 3

    def live(self, organism):
        organism.health += self.food
        self.food -= 1


my_organism = organism()
my_env = environment()

for (years in range(10)):
    my_env.live(organism)
    if organism.death == true:
        break
    elif organism.reproduce== true:
        logging.debug("reproducing"!)
