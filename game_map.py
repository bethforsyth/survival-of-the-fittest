import pygame

window_height = 1000
window_length = 1000
pygame.init()
screen = pygame.display.set_mode((window_height, window_length))
GREEN = (0, 200, 0)
RED = (200, 0, 0)


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


def draw_map(environment, orgs):
    square_size = (window_length / environment.size)
    for row in environment.grid:
        for location in row:
            draw_square(location, square_size)
    pygame.display.update()
