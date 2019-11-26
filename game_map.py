import pygame

window_height = 400
window_length = 400
pygame.init()
screen = pygame.display.set_mode((window_height, window_length))
GREEN = (0, 200, 0)
RED = (200, 0, 0)

def draw_square(x, y, square_size):
    pygame.draw.rect(screen, GREEN, (x, y, square_size, square_size))
    pygame.draw.rect(screen, RED, (x, y, square_size, square_size), 1)

def draw_map(environment, orgs):
    square_size = (window_length/environment.size)
    for row in environment.grid:
        for location in row:
            x_coord = location.xpos * (window_length/environment.size)
            y_coord = location.ypos * (window_height/environment.size)
            draw_square(x_coord, y_coord, square_size)
    pygame.display.update()
