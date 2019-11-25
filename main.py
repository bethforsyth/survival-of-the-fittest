import logging
import copy

class organism:
    def __init__(self):
        self.code = "0001011010101"
        self.size = 10
        self.health = 5
        self.dead = False


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
        # Turn the genetic code into characteristics.
        return


class environment:
    def __init__(self):
        self.food = 3

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







<<<<<<< HEAD
#test pushing x2
=======
>>>>>>> cb266f10defe86e79e7648e53c46db99cbe028e4
