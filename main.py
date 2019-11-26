import logging
import copy
import random
from base_genome import BASE_GENOME


class organism:
    def __init__(self):
        self.code = BASE_GENOME
        for j in range(800):
            self.code.append(random.randint(0, 9))
        logging.debug("Code is {}".format(self.code))
        self.size = 10
        self.health = 10
        self.dead = False

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
                logging.debug("Reproducing")

                # Giving birth costs health.
                org.health -= 1

                # Create a baby! Obviously the baby is born with full health.
                new_org = copy.deepcopy(org)
                new_org.health = 10
                new_orgs.append(new_org)
        self.organisms += new_orgs

    def mutate(self):
        return

    def translation(self):
        for org in self.organisms:
            org.get_genes()


class environment:

    def __init__(self):
        self.food = 30

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
    logging.debug("we have {}".format(len(organisms.organisms)))
