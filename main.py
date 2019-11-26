import logging
import copy
import random
from base_genome import BASE_GENOME

## Traits are not particular to a specific organism, and must interact
## with the environment as well as the organism, so we'll define them  in a

class gene_struct:
    def __init__(self):
        self.index = 0
        self.operator = 0
        self.binding = 0
        self.quantifier = 0

## These must not overlap!
traits = {"123": "size", "456": "metabolism"}
stimuli = {"043": "temperature", "375": "food"}

class organism:
    def __init__(self):
        self.code = BASE_GENOME
        for j in range(800):
            self.code.append(random.randint(0, 9))
        logging.debug("Code is {}".format(self.code))
        self.size = 10
        self.health = 10
        self.dead = False
        self.traits = {"size": 1, "metabolism": 1}

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
        gene_traits = []

        for gene in self.genes:
            my_gene = gene_struct()
            ## Genes are structures where
            ## pos 0-2 is the start codon
            ## pos 3-5 is the gene index (which tells us whether this
            ## is a trait, sensory, or regulatory)
            ## pos 6-8 is the operator
            ## pos 9-11 is binding site
            ## the rest to the end is the quantifier

            ## getting occasional run-time errors here, and I'm not quite sure why - possibly too long?
            my_gene.index = "".join(map(str, gene[3:6]))
            my_gene.operator = int("".join(map(str, gene[6:9])))
            my_gene.binding = int("".join(map(str, gene[9:12]))) 
            my_gene.quantifier = int("".join(map(str, gene[12:]))) 

            gene_traits.append(my_gene)

        self.gene_traits = gene_traits

    def apply_sensory(self, environment):
        for gene in self.gene_traits:
            if is_sensory(gene.index):
                for other_gene in self.gene_traits:
                    if binds(gene.binding, other_gene.binding) and not is_sensory(other_gene.index):
                        stimulus = environment.get_stimulus(gene.index)
                        new_quantifier = apply_operator(gene.operator, stimulus*gene.quantifier, other_gene.quantifiers)
                        other_gene.quantifier = new_quantifier

    def apply_regulatory(self):
        for gene in self.gene_traits:
            if not is_sensory(gene.index) and  not is_trait(gene.index):
                for other_gene in self.gene_traits:
                    if is_trait(other_gene.index) and binds(gene.binding, other_gene.binding):
                        new_quantifier = apply_operator(gene.operator, gene.quantifier, other_gene.quantifiers)
                        other_gene.quantifier = new_quantifier

    def apply_trait(self):
        for gene in self.gene_traits:
            if is_trait(gene.index):
                self.apply_operator_to_trait(gene.index, gene.operator, gene.quantifier, gene.index)



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

def is_sensory(index):
    if index in stimuli:
        return True
    else:
        return False

def is_trait(index):
    if index in traits:
        return True
    else:
        return False

def apply_operator_to_trait(self, index, operator, quantifier):
    ## We should at this point be sure that the index corresponds to a valid trait
    trait_type = traits[index]
    self.traits[trait_type] = apply_operator(operator, quantifier, self.traits[trait_type])

def binds(codon1, codon2):
    if codon1 == codon2:
        return True
    else:
        return False

def apply_operator(operator, quantifier, target):
    ## We're going to make 
    if operator < 250:
        return target + quantifier

    elif operator >= 205 and operator < 500 :
        return target - quantifier

    elif operator >=500 and operator < 750 :
        return target * (quantifier / 100)
    else :
        return target / (quantifier / 100)

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

    def translation(self, environment):
        for org in self.organisms:
            org.get_genes()
            org.genes_to_traits()
            org.apply_sensory(environment)
            org.apply_regulatory()
            org.apply_trait()


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


logging.basicConfig(level=logging.ERROR)
logging.debug("Starting!")

environ = environment()
organisms = orgs()
for years in range(10):
    logging.debug("loop number {}!".format(years))
    organisms.mutate()
    organisms.translation(environ)

    environ.main(organisms)

    organisms.death()
    organisms.reproduce()
    logging.debug("we have {}".format(len(organisms.organisms)))
