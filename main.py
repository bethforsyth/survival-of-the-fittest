import logging
import copy
import random


class organism:
    def __init__(self):
        self.code = []
        for j in range(1000):
            self.code.append(random.randint(0, 9))
        logging.debug("Code is {}".format(self.code))
        self.size = 10
        self.health = 10
        self.dead = False

    def get_genes(self):
        genes = []
        start_pos = 0
        end_pos = 0
        codon = [0, 0, 0]
        in_gene = False
        for i in range(2, len(self.code)):
            codon[0] = self.code[i - 2]
            codon[1] = self.code[i - 1]
            codon[2] = self.code[i]
            if is_start_codon(codon) and not in_gene:
                in_gene = True
                start_pos = i - 2
            elif is_end_codon(codon) and in_gene:
                end_pos = i
                in_gene = False
                genes.append(self.code[start_pos:end_pos])
        return genes


# This should give us the start of a gene approximately 1/100 codons.
def is_start_codon(codon):
    if codon[0] == 0 and codon[1] == 1:
        print"START"
        return True
    else:
        return False


# This should give us the end of a gene approximately 1/100 codons.
def is_end_codon(codon):
    if codon[0] == 9 and codon[1] == 8:
        print("END")
        return True
    else:
        return False


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
                # logging.debug("Reproducing")
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
            genes = org.get_genes()
            for gene in genes:
                print(gene)


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
