import logging
import copy
import random

## Traits are not particular to a specific organism, and must interact
## with the environment as well as the organism, so we'll define them  in a

class gene_traits:
    def __init__(self):
        self.index = 0
        self.operator = 0
        self.binding = 0
        self.quantifier = 0

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
        self.genes = []
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
                self.genes.append(self.code[start_pos:end_pos])
        return self.genes

    def genes_to_traits(self):
        gene_behaviours = []

        for gene in self.genes:
            my_gene = gene_traits()
            ## Genes are structures where
            ## pos 0-2 is the start codon
            ## pos 3-5 is the gene index (which tells us whether this
            ## is a trait, sensory, or regulatory)
            ## pos 6-8 is the operator
            ## pos 9-11 is binding site
            ## the rest to the end is the quantifier
            my_gene.index = int("".join(map(str, gene[3:6]))) 
            my_gene.operator = int("".join(map(str, gene[6:9]))) 
            my_gene.binding = int("".join(map(str, gene[9:12]))) 
            my_gene.quantifier = int("".join(map(str, gene[12:]))) 


            gene_behaviours.append(my_gene)



# This should give us the start of a gene approximately 1/100 codons.
def is_start_codon(codon):
    if codon[0] == 0 and codon[1] == 1:
        return True
    else:
        return False


# This should give us the end of a gene approximately 1/100 codons.
def is_end_codon(codon):
    if codon[0] == 9 and codon[1] == 8:
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
            org.genes_to_traits()


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
