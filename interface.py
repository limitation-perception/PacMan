import pygame
WIDTH = 950
HEIGHT = 900
pygame.init()
pygame.display.set_mode((WIDTH,  HEIGHT))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

