import pygame
from boards_for_levels import boards
import math
pygame.init()

WIDTH = 700
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
fps = 60
timer = pygame.time.Clock()
# font = pygame.font.Font("", 32)      HAVE TO ADD LATER!!!!!!!!!
level1 = boards
color_for_walls = 'blue'
color_for_food = 'white'

PI = math.pi
def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level1)):
        for j in range(len(level1[i])):
            if level1[i][j] == 1:
                pygame.draw.circle(screen, color_for_food, (j * num2 + (0.5*num2), i * num1 +(0.5*num1)),
                                   4)
            if level1[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 +(0.5*num1)),
                                   8)
            if level1[i][j] == 3:
                pygame.draw.line(screen, color_for_walls, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + 0.5 * num2, i * num1 + num1), 3)
            if level1[i][j] == 4:
                pygame.draw.line(screen, color_for_walls,(j * num2, i * num1 +(0.5*num1)),
                                 (j * num2 + num2, i * num1 +(0.5*num1)), 3)
            if level1[i][j] == 5:
                pygame.draw.arc(screen, color_for_walls, [(j*num2 - 0.4 * num2), (i*num1 + 0.5*num1),
                                                          num2, num1], 0, PI/2, 3)
            if level1[i][j] == 6:
                pygame.draw.arc(screen, color_for_walls, [(j*num2 + 0.5 * num2), (i*num1 + 0.5*num1),
                                                          num2, num1], PI/2, -PI, 3)
            if level1[i][j] == 7:
                pygame.draw.arc(screen, color_for_walls, [(j*num2 + 0.5 * num2), (i*num1 - 0.4*num1),
                                                          num2, num1], -PI, -PI/2, 3)
            if level1[i][j] == 8:
                pygame.draw.arc(screen, color_for_walls, [(j*num2 - 0.4 * num2), (i*num1-0.4*num1),
                                                          num2, num1], -PI/2, 0, 3)
            if level1[i][j] == 9:
                pygame.draw.line(screen, 'white',(j * num2, i * num1 +(0.5*num1)),
                                 (j * num2 + num2, i * num1 +(0.5*num1)), 3)

def draw_pacman()

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board()
    draw_pacman()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
