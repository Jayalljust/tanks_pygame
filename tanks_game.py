import pygame
import sys
from tank import Tank

def run():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Танчики')
    bg_color = (0,0,0)
    tank = Tank(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        tank.display()
        pygame.display.flip()

run()
