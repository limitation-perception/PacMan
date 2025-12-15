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
pacman_images = []
for i in range(1,5):
    pacman_images.append(pygame.transform.scale(pygame.image.load(f'pacman_images/{i}.png'), (115, 115)))


def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level1)):
        for j in range(len(level1[i])):
            if level1[i][j] == 1:
                pygame.draw.circle(screen, color_for_food, (j * num2 + (0.5*num2), i * num1 +(0.5*num1)),
                                   3)
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



pacman_start_x = 299
pacman_start_y = 455
direction = 0
counter = 0
def draw_pacman():
    # 0 = RIGHT     1 = LEFT    2 = UP      3 = DOWN
    if direction == 0:
        screen.blit(pacman_images[counter // 5], (pacman_start_x, pacman_start_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(pacman_images[counter // 5],True, False), (pacman_start_x, pacman_start_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 5], 90), (pacman_start_x, pacman_start_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 5], -90), (pacman_start_x, pacman_start_y))

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter +=1
    else:
        counter = 0

    screen.fill('black')
    draw_board()
    draw_pacman()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3


    pygame.display.flip()
pygame.quit()
