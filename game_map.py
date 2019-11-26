import pygame

window_height = 800
window_length = 800
pygame.init()
screen = pygame.display.set_mode((window_height, window_length))
GREEN = (0, 200, 0)
RED = (200, 0, 0)
ANIMAL_BROWN = (150, 75, 0)
FOOD_COLOR = (228,180,34)


def get_terrain_colour(terrain):
    colour = (0, 0, 0)
    if terrain == 'grass':
        colour = (34, 139, 34)
    elif terrain == 'sand':
        colour = (237, 217, 175)
    elif terrain == 'snow':
        colour = (255, 255, 255)
    return colour


def get_temp_colour(temperature):
    cold = [36, 0, 134]
    hot = [255, 0, 0]
    colour = [0, 0, 0]
    for i in range(3):
        colour[i] = cold[i] + ((temperature + 20) / 60) * (hot[i] - cold[i])
    return colour


def draw_square(location, square_size):
    x = location.xpos * square_size
    y = location.ypos * square_size
    terrain_colour = get_terrain_colour(location.terrain)
    pygame.draw.rect(screen, terrain_colour, (x, y, square_size, square_size))
    temperature_colour = get_temp_colour(location.temperature)
    pygame.draw.rect(screen, temperature_colour, (x, y, square_size, square_size), 1)


def draw_animals(animal_list, square_size, locx, locy):
    num_animals = len(animal_list)
    print("There are {} animals".format(num_animals))
    print("coords are {} and {}".format(locx, locy))
    animal_in_queue = 1
    for animal in animal_list:
        x = int((animal_in_queue % 5) * square_size/5 + square_size/10 + locx)
        y = int(int(animal_in_queue / 5) * square_size/5 + square_size/10 + locy)
        print("x = {} and y = {}".format(x, y))
        pygame.draw.circle(screen, ANIMAL_BROWN, (x,y), int(square_size/12))
        animal_in_queue += 1


def draw_plant_food(food, square_size, locx, locy):
    print("There is {} food".format(int(round(food))))
    print("coords are {} and {}".format(locx, locy))
    food_in_queue = 1
    print("food:", food)
    food_range = int(round(food))
    for food_item in range(food_range):
        x = int((food_in_queue % 5) * square_size/10 + square_size/20 + locx)
        y = int(int(food_in_queue / 5) * square_size/10 + square_size/20 + locy)
        print("x = {} and y = {}".format(x, y))
        pygame.draw.circle(screen, FOOD_COLOR, (x,y), int(square_size/30))
        food_in_queue += 1


def draw_map(environment, orgs):
    square_size = (window_length / environment.size)
    for row in environment.grid:
        for location in row:
            x_coord = location.xpos * (window_length/environment.size)
            y_coord = location.ypos * (window_height/environment.size)
            draw_square(location, square_size)
            draw_animals(location.organisms_list, square_size, x_coord, y_coord)
            draw_plant_food(location.traits["plant_food"], square_size, x_coord, y_coord)
    pygame.display.update()
