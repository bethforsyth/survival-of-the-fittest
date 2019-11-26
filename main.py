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
        self.current_pos = environment.location[start_posx][start_posy]


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


# month = 1
# if month > 12:
#     month-=12
# temperature = 20-((month-6)^2)/4


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
<<<<<<< HEAD






<<<<<<< HEAD
#test pushing x2
=======
>>>>>>> cb266f10defe86e79e7648e53c46db99cbe028e4
=======
>>>>>>> d46e7d3d789d639fb3e64bdfa4d06681f459bf89
