import logging
import copy
import random
from environment import environment

environ = environment()


class organism:
    def __init__(self):
        self.code = "0001011010101"
        self.traits = {"size":10, "strength":6, "speed":2, "greediness":8, "intelligence":10}
        self.health = 10
        self.dead = False
        self.start_posx = 1  #random.randint(0, 7)
        self.start_posy = 1  #random.randint(0, 7)
        self.current_pos = (self.start_posx, self.start_posy)


class orgs:
    def __init__(self):
        self.organisms = [organism() for i in range(1)]

    def death(self):
        new_orgs = []
        for org in self.organisms:
            if org.health > 0:
                new_orgs.append(org)
            else:
                logging.debug("An organism dies")
        self.organisms = new_orgs

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
        #for each organism (some percentage get the mutation applied)

        for org in self.organisms:
            logging.debug("Mutating")

        #Randomly select a trait and randomly increment or decrement the size
        #trait by 1.

            # random_trait = random.choice(list(org.traits))
            # print(random_trait)
            # if random.choice([1, 2]) == 1:
            #     org.traits[random_trait] += 1
            # else:
            #     org.traits[random_trait] -= 1

        #different versions of mutating genetic code
        # choose which mutation
            if random.randint(1, 4) == 1:
                #duplication
                logging.debug("duplication mutation")
            elif random.randint(1, 4) == 2:
                logging.debug("delete mutation")

                def mutate_deletion(self):
                    code_as_list = []
                    for digit in org.code:
                        code_as_list.append(digit)
                    code_as_list.pop(random.randrange(len(code_as_list)))
                    return "".join(code_as_list)
                mutate_deletion(self)

            elif random.randint(1, 4) == 3:
                #add
                logging.debug("addition mutation")

            else:
                #change
                logging.debug("change mutation")

    def translation(self):
        # Turn the genetic code into characteristics.
        return

class environment:
    def __init__(self):
        self.food = 30

    def position(self, location_id=1, x=0, y=0, temperature=0):
        global location
        location=[location_id, x, y, temperature]
        counter1=0
        counter2=0
        counter3=0
        while counter2<21:
            environment.append(position(counter3, counter1, counter2).location)
            counter1+=1
            counter3+=1

            if counter1>20:
                counter1-=20
                counter2+=1

    def main(self, organisms):
        # Anything in environment that needs to change (e.g. plants grow)

        # Environment acts on organisms

        return

    def live(self, organisms):
        for num in range(len(organisms.organisms)):
            organism = organisms.organisms[num]
            organism.health += self.food
            self.food -= 1

    # def count_organisms_at_pos:
    #     self.posx = 0
    #     self.posy = 0
    #     self.cur_check = position[self.posx][self.posy]
    #     if :



# month = 1
# if month > 12:
#     month-=12
# temperature = 20-((month-6)^2)/4

    def eat(self):
        '''Loop through organisms and get them to eat if there is food'''
        # always eat plants
        logging.debug("Eating")
        for org in self.organisms:
            if environ.location(org.current_pos).plant_food > 0:
                environ.location(org.current_pos).plant_food -= 1
                logging.debug("The current food is {}".format(environ.location(org.current_pos).plant_food))
            else:
                org.health -= 1


logging.basicConfig(level=logging.DEBUG)
logging.debug("Starting!")

organisms = orgs()
for years in range(10):
    logging.debug("loop number {}!".format(years))
    organisms.mutate()
    organisms.translation()

    environ.main(organisms)
    # organisms.eat()
    organisms.death()
    organisms.reproduce()

    logging.debug("we have {}".format(len(organisms.organisms)))
