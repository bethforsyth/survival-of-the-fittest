import logging
import copy
import random
from base_genome import BASE_GENOME
from environment import environment

## Traits are not particular to a specific organism, and must interact
## with the environment as well as the organism, so we'll define them  in a

class gene_struct:
    def __init__(self):
        self.index = 0
        self.operator = 0
        self.binding = 0
        self.quantifier = 0

environ = environment()

## These must not overlap!
## should correspond to organism
traits = {"032": "strength", "122": "size", "452": "metabolism", "502": "speed", "662": "greediness", "682": "intelligence"}


class organism:
    def __init__(self):
        self.code = BASE_GENOME
        for j in range(800):
            self.code.append(random.randint(0, 9))
        logging.debug("Code is {}".format(self.code))
        self.code = "0001011010101"
        self.traits = {"size": 10, "strength": 6, "metabolism": 6, "speed": 2, "greediness": 8, "intelligence": 10}
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
                in_gene = Truel
            elif is_end_codon(self.code[i - 2], self.code[i - 1]) and in_gene:
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
                        loc = environment(location(self.current_pos))
                        stimulus = get_stimulus(gene.index)
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

# This should give us the start of a gene approximately 1/100 codons.
def is_start_codon(first_base, second_base):
    if first_base == 0 and second_base == 1:
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
        logging.debug("Translating!")
        for org in self.organisms:
            org.get_genes()
            org.genes_to_traits()
            org.apply_sensory(environ)
            org.apply_regulatory()
            org.apply_trait()

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
