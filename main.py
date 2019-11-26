import logging
import copy
import random

class organism:
    def __init__(self):
        self.code = "0001011010101"
        self.traits = {"size":10, "strength":6, "speed":2, "greediness":8, "intelligence":10}
        self.health = 10
        self.dead = False
        self.start_posx = random.randint(5,15)
        self.start_posy = random.randint(5,15)
        self.current_pos = environment.location[self.start_posx][self.start_posy]


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
        new_orgs = []
        for org in self.organisms:
            if org.health > 6:
                # Giving birth costs health.
                org.health -= 1

                # Create a baby! Obviously the baby is born with full health.
                new_org = copy.deepcopy(org)
                new_org.health = 10
                new_orgs.append(new_org)
        self.organisms += new_orgs

    def mutate(self):
        '''
        Randomly select a trait and randomly increment or decrement the size
        trait by 1. Randomly. '''
        #for each organism (some percentage get the murtation applied)

        for org in self.organisms:
            logging.debug("Mutating")
            random_trait = random.choice(list(org.traits))
            print(random_trait)
            if random.choice([1, 2]) == 1:
                org.traits[random_trait] += 1
            else:
                org.traits[random_trait] -= 1

    def translation(self):
        # Turn the genetic code into characteristics.
        return

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

    logging.debug("we have {}".format(len(organisms.organisms)))
