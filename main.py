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
traits = {"032": "strength", "123": "size", "456": "metabolism", "503": "speed", "666": "greediness", "689": "intelligence"}
stimuli = {"043": "temperature", "375": "food"}

class organism:
    def __init__(self):
        self.code = BASE_GENOME
        for j in range(800):
            self.code.append(random.randint(0, 9))
        logging.debug("Code is {}".format(self.code))
        self.code = "001234567890123""
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
                in_gene = True
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
        Randomly select a type of mutation (duplication, deletion, addition or
        code change) and apply to each organism.'''
        #for each organism (some percentage get the mutation applied)

        for org in self.organisms:
            logging.debug("Mutating")
            if random.randint(1, 4) == 1:
                logging.debug("Duplicating DNA")
###############################################################################
#           Duplication mutation                                              #
###############################################################################
                def mutate_duplicate(self):
                    '''
                    Duplicate piece of organism's code inbetween random indices.
                    '''
                    logging.debug("duplicate mutation")
                    random_index1 = random.randint(0,len(org.code)-1)
                    random_index2 = random.randint(0,len(org.code)-1)
                    start_index = min(random_index1, random_index2)
                    end_index = max(random_index1, random_index2)

                    #length_of_copy = end_index-start_index
                    mutated_code = (org.code[:start_index] +
                        org.code[start_index:end_index]*2 + org.code[end_index:])
                    #print("Old code: ", org.code, "\nNew code: ", mutated_code, "(Duplicated from %d to %d)"%(start_index, end_index))
                    return(mutated_code)
                mutate_duplicate(self)

            elif random.randint(1, 4) == 2:
                logging.debug("delete mutation")
###############################################################################
#           Deletion mutation                                                 #
###############################################################################
                def mutate_deletion(self):
                    '''
                    Randomly delete one of the digits from the organism's code.
                    '''
                    code_as_list = []
                    for digit in org.code:
                        code_as_list.append(digit)

                    random_index1 = random.randint(0,len(org.code)-1)
                    random_index2 = random.randint(0,len(org.code)-1)
                    start_index = min(random_index1, random_index2)
                    end_index = max(random_index1, random_index2)

                    print("start, end are", start_index, end_index)
                    for index in range(end_index, start_index, -1):
                        print("length of code_as_list is ", len(code_as_list), "index is ", index)
                        del code_as_list[index]
                    mutated_code = "".join(code_as_list)
                    print('\n', org.code, 'is the original code\n', mutated_code, 'is the mutated code')
                    org.code = mutated_code
                    return mutated_code
                mutate_deletion(self)

            elif random.randint(1, 4) == 3:
                logging.debug("addition mutation")

###############################################################################
#           Addition mutation                                                 #
###############################################################################
                def addition_mutation(self):
                    '''
                    Add a new digit to a random place in the organism's code.
                    '''
                    code_as_list = list(org.code)
                    code_as_list.insert(random.randint(0, len(org.code)), str(random.randint(0,9)))
                    new_code = ''.join(code_as_list)
                    #print("original code: " + org.code + " mutated code:" + new_code)
                    return new_code

                addition_mutation(self)

            else:
                logging.debug("change mutation")
###############################################################################
#           Change mutation                                                   #
###############################################################################
                def change_mutation(self):
                    '''
                    Change a random slice of the organism's code to a random
                    string of 1s and 0s.
                    '''
                    random_length = random.randint(0, len(org.code))
                    random_index = random.randint(0, len(org.code)-1)

                    print("original code:", org.code)
                    print("changing " + str(random_length) + " nucleotides at index " + str(random_index))
                    new_code = []
                    new_code_str = ""
                    for i in range(random_length):
                        new_code.append(str(random.randint(0,9)))
                        new_code_str = "".join(new_code)

                    org.code = org.code[:random_index] + new_code_str + org.code[random_index + (random_length -1):]
                    print("new_code:", org.code)
                    return org.code
                change_mutation(self)


    def translation(self):
        # Turn the genetic code into characteristics.
        for org in self.organisms:
            org.get_genes()
            org.genes_to_traits()
            org.apply_sensory(environment)
            org.apply_regulatory()
            org.apply_trait()

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
