import logging
import copy

class organism:
    def __init__(self):
        self.code = "0001011010101"
        self.size = 10
        self.health = 5
        self.dead = False


class orgs:
    def __init__(self):
        self.organisms = [organism() for i in range(1)]

    def death(self):
        list_index = 0
        for org in self.organisms:
            if org.health <= 0:
                logging.debug("Dying")
                del self.organisms[list_index]
            else:
                list_index += 1

    def reproduce(self):
        for org in self.organisms:
            if org.health > 6:
                logging.debug("Reproducing")
                new_org = copy.deepcopy(org)
                self.organisms.append(new_org)

    def mutate(self):
        return

    def translation(self):
        # Turn the genetic code into characteristics.
        return


class environment:

    def __init__(self):
        self.food = 3

    def main(self, organisms):
        # Anything in environment that needs to change (e.g. plants grow)

        # Environment acts on organisms
        return


    def live(self, organisms):
        for num in range(len(organisms.organisms)):
            organism = organisms.organisms[num]
            organism.health += self.food
            self.food -= 1



logging.basicConfig(level=logging.DEBUG)
logging.debug("Starting!")

environ = environment()
organisms = orgs()
for years in range(10):
    logging.debug("loop number {}!".format(years))
    organisms.mutate()
    organisms.translation()

    environ.main(organisms)

    organisms.death()
    organisms.reproduce()







