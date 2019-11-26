import logging
import copy
import random
import math
from environment import environment

environ = environment()


class organism:
    def __init__(self):
        self.code = "0001011010101"
        self.traits = {"size":10, "strength":6, "speed":2, "greediness":8, "intelligence":10}
        self.health = 10
        self.dead = False
        self.start_posx = random.randint(0, 7)
        self.start_posy = random.randint(0, 7)
        self.current_pos = [self.start_posx, self.start_posy]
        (environ.location(self.current_pos)).organisms_list.append(self)

class orgs:
    def __init__(self):
        self.organisms = [organism() for i in range(1)]

    def death(self):
        new_orgs = []
        number_of_deaths=0
        for org in self.organisms:
            if org.health > 0:
                new_orgs.append(org)
            else:
                number_of_deaths+=1
        logging.debug(f"{number_of_deaths} organisms died")
        self.organisms = new_orgs

    def reproduce(self):
        new_orgs = []
        for org in self.organisms:
            if org.health > 6:
                # Giving birth costs health.
                org.health -= 1

                # Create a baby! Obviously the baby is born with full health.
                new_org = organism()
                new_org.start_posx = random.randint(0, 7)
                new_org.start_posy = random.randint(0, 7)
                new_org.health = 10
                new_orgs.append(new_org)
        self.organisms += new_orgs

    # def move(self):
    #     for org in self.organisms:
    #         self.move_x=random.randint(-org.traits.get("speed")+1, org.traits.get("speed")+1)
    #         self.move_y=random.randint(-org.traits.get("speed")+1, org.traits.get("speed")+1)
    #         self.new_posx = org.current_pos[0] + self.move_x
    #         self.new_posy = org.current_pos[1] + self.move_y
    #         if self.new_posx > 0 and self.new_posx < environ.size and self.new_posy > 0 and self.new_posy < environ.size:
    #             self.current_pos = (self.new_posx, self.new_posy)
    #         (environ.location(self.current_pos)).organisms_list_after_move.append(self)

    #     for x in range(0, environ.size):
    #         for y in range(0, environ.size):
    #             environ.location(self.current_pos).organisms_list=environ.location(self.current_pos).organisms_list_after_move
    #             environ.location(self.current_pos).organisms_list_after_move=[]

    def mutate(self):
        '''
        Randomly select a trait and randomly increment or decrement the size
        trait by 1. Randomly. '''
        #for each organism (some percentage get the murtation applied)

        for org in self.organisms:
            #logging.debug("Mutating")
            random_trait = random.choice(list(org.traits))
            #print(random_trait)
            if random.choice([1, 2]) == 1:
                org.traits[random_trait] += 1
            else:
                org.traits[random_trait] -= 1

    def translation(self):
        # Turn the genetic code into characteristics.
        return

    def eat(self):
        '''Loop through organisms and get them to eat if there is food'''
        # always eat plants
        logging.debug("Eating")
        for org in self.organisms:
            food_consump = math.floor(org.traits.get("size")/4)
            if environ.location(org.current_pos).plant_food >= food_consump:
                environ.location(org.current_pos).plant_food -= food_consump
                # logging.debug("The current food is {}".format(environ.location(org.current_pos).plant_food))
                org.health += round(food_consump/2) + 1
            else:
                org.health -= 4

    def environment_effect(self):
        for org in self.organisms:
            self.temperature_range_min = self.size*(-2)
            self.temperature_range_max = 45 - self.size * 2
            if environ.location(org.current_pos).temperature < self.temperature_range_min:
                org.health -= math.round(self.temperature_range_min-environ.location(org.current_pos).temperature)
            elif environ.location(org.current_pos).temperature < self.temperature_range_max:
                org.health -= math.round(self.temperature_range_max-environ.location(org.current_pos).temperature)

logging.basicConfig(level=logging.DEBUG)
logging.debug("Starting!")

organisms = orgs()
for years in range(10):
    logging.debug("loop number {}!".format(years))
    organisms.mutate()
    organisms.translation()

    environ.main(organisms)
    organisms.eat()
    organisms.death()
    organisms.reproduce()
    # organisms.move()

    environ.grow_plants()
    environ.count_organisms(organisms)
    logging.debug("we have {} organisms in position 2,2".format(environ.location((2, 2)).organism_number))
    logging.debug("we have {}".format(len(organisms.organisms)))
