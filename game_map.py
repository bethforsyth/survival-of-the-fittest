import pygame

window_height = 1000
window_length = 1000
pygame.init()
screen = pygame.display.set_mode((window_height, window_length))
GREEN = (0, 200, 0)
RED = (200, 0, 0)
ANIMAL_BROWN = (150, 75, 0)

def draw_square(x, y, square_size):
    pygame.draw.rect(screen, GREEN, (x, y, square_size, square_size))
    pygame.draw.rect(screen, RED, (x, y, square_size, square_size), 1)

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


def draw_map(environment, orgs):
    square_size = (window_length/environment.size)
    for row in environment.grid:
        for location in row:
            x_coord = location.xpos * (window_length/environment.size)
            y_coord = location.ypos * (window_height/environment.size)
            draw_square(x_coord, y_coord, square_size)
            draw_animals(location.organisms_list, square_size, x_coord, y_coord)
    pygame.display.update()
