import logging
import copy
import random
from environment import environment

environ = environment()


class organism:
    def __init__(self):
        self.code = "01234567890123"
        self.traits = {"size":10, "strength":6, "speed":2, "greediness":8, "intelligence":10}
        # self.size = 10
        self.health = 5
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
                    random_dup_index1 = random.randint(0,len(org.code)-1)
                    random_dup_index2 = random.randint(0,len(org.code)-1)
                    start_index = min(random_dup_index1, random_dup_index2)
                    end_index = max(random_dup_index1, random_dup_index2)
                    #length_of_copy = end_index-start_index
                    mutated_code = (org.code[:start_index] +
                        org.code[start_index:end_index]*2 + org.code[end_index:])
                    print("Old code: ", org.code, "\nNew code: ", mutated_code, "(Duplicated from %d to %d)"%(start_index, end_index))
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
                    code_as_list.pop(random.randrange(len(code_as_list)))
                    print("original code: " + org.code + " mutated code:" + ("".join(code_as_list)))
                    return "".join(code_as_list)
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
                    print("original code: " + org.code + " mutated code:" + new_code)
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
