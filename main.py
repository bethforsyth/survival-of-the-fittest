import logging
import copy
import random
from base_genome import BASE_GENOME
from environment import environment

environ = environment()

class organism:
    def __init__(self):
        self.code = BASE_GENOME
        for j in range(800):
            self.code.append(random.randint(0, 9))
        logging.debug("Code is {}".format(self.code))
        self.code = "0001011010101"
        self.traits = {"size": 10, "strength": 6, "speed": 2, "greediness": 8, "intelligence": 10}
        self.health = 10
        self.dead = False
        self.start_posx = 1  #random.randint(0, 7)
        self.start_posy = 1  #random.randint(0, 7)
        self.current_pos = (self.start_posx, self.start_posy)

    def get_genes(self):
        self.genes = []
        start_pos = 0
        end_pos = 0
        in_gene = False
        for i in range(2, len(self.code)):
            if is_start_codon(self.code[i - 2], self.code[i - 1]) and not in_gene:
                start_pos = i - 2
                in_gene = True
            elif is_end_codon(self.code[i - 2], self.code[i - 1]) and in_gene:
                end_pos = i
                in_gene = False
                self.genes.append(self.code[start_pos:end_pos])
        return self.genes


# This should give us the start of a gene approximately 1/100 codons.
def is_start_codon(first_base, second_base):
    if first_base == 0 and second_base == 1:
        return True
    else:
        return False


# This should give us the end of a gene approximately 1/100 codons.
def is_end_codon(first_base, second_base):
    if first_base == 0 and second_base == 1:
        return True
    else:
        return False


class orgs:
    def __init__(self):
        self.organisms = [organism() for i in range(2)]

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
        for org in self.organisms:
            org.get_genes()

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
    organisms.eat()
    organisms.death()
    organisms.reproduce()


    logging.debug("we have {}".format(len(organisms.organisms)))
