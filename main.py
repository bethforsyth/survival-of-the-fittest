import logging
import copy
import random

class organism:
    def __init__(self):
        self.code = []
        for j in range(1000):
            self.code.append(random.randint(0,9))
        logging.debug("Code is {}".format(self.code))
        self.size = 10
        self.health = 5
        self.dead = False

    def get_genes(self):
        genes = [[]]
        start_pos = 0
        end_pos = 0
        codon = [0,0,0]
        in_gene = False
        for i in range(len(self.code)):
            codon[(i%3)]= self.code[i]
            if i%3 == 2:
                # Got a full codon, check what it's doing
                if is_start_codon(codon) and in_gene == False:
                    in_gene = True
                    start_pos = i-3
                elif is_end_codon(codon) and in_gene == True:
                    end_pos = i
                    in_gene = False
                    genes.append = [self.code[start_pos:end_pos]]

        print(genes)
        return genes



## This should give us the start of a gene approximately
## 1/100 codons.
def is_start_codon(codon):
    if codon[0] == 0 and codon[1] == 1:
        True
    else:
        False

## This should give us the end of a gene approximately
## 1/100 codons.
def is_end_codon(codon):
    if codon[0] == 9 and codon[1] == 8:
        True
    else:
        False

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
        for org in self.organisms:
            org.get_genes()
            print("Got genes!")


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







