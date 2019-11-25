import logging

class organism:
    def __init__(self):
        self.code = "0001011010101"
        self.size = 10
        self.health = 5
        self.dead = False

class organisms:
    def __init__(self):
        self.organisms = [organism() for i in range(1)]

    def death(self):
        for num in range(len(self.organisms)):
            my_organism = self.organisms[num]
            if my_organism.health < 4:
                logging.debug("Dying")
                my_organism.dead = True

    def reproduce(self):
        for num in range(len(self.organisms)):
            my_organism = self.organisms[num]
            if (my_organism.health > 6 and my_organism.dead )== False:
                logging.debug("Reproducing")
                self.organisms.append(organism())
                return True

class environment:

    def __init__(self):
        self.food = 3

    def live(self, organisms):
        for num in range(len(organisms.organisms)):
            organism = organisms.organisms[num]
            organism.health += self.food
            self.food -= 1


logging.basicConfig(level=logging.DEBUG)
logging.debug("Starting!")

my_organisms = organisms()
my_env = environment()

for years in range(10):
    logging.debug("loop number {}!".format(years))
    my_env.live(my_organisms)
    my_organisms.death()
    my_organisms.reproduce()
