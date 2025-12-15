import pygame
from pygame import FULLSCREEN

from boards_for_levels import boards
import math
pygame.init()

WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode((WIDTH, HEIGHT) ) # FULLSCREEN???
fps = 60
timer = pygame.time.Clock()
# font = pygame.font.Font("", 32)      HAVE TO ADD LATER!!!!!!!!!
level1 = boards
color_for_walls = 'blue'
color_for_food = 'white'
PI = math.pi
pacman_images = []
for i in range(1,5):
    pacman_images.append(pygame.transform.scale(pygame.image.load(f'packman_images/{i}.png'), (45, 45)))

pacman_start_x = 450
pacman_start_y = 663
direction = 0
counter = 0
flicker = False
turns_allowed = [False, False, False, False]

def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level1)):
        for j in range(len(level1[i])):
            if level1[i][j] == 1:
                pygame.draw.circle(screen, color_for_food, (j * num2 + (0.5*num2), i * num1 +(0.5*num1)),
                                   4)
            if level1[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 +(0.5*num1)),
                                   10)
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

def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (HEIGHT - 50) // 32
    num2 = WIDTH // 30
    num3 = 15

    if centerx // 30 < 29:
        if direction == 0:
            if level1[centery // num1][(centerx - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if level1[centery // num1][(centerx + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if level1[(centery + num3) // num1][centerx // num2] < 3:
                turns[3] = True
        if direction == 3:
            if level1[(centery - num3) // num1][centerx // num2] < 3:
                turns[2] = True


        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level1[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level1[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level1[centery // num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level1[centery // num1][(centerx + num2) // num2] < 3:
                    turns[0] = True


        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level1[(centery + num1) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level1[(centery - num1) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level1[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
                if level1[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True



    else:
        turns[0] = True
        turns[1] = True

    return turns

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter +=1
        if counter > 3:
         flicker = False
    else:
        counter = 0
        flicker = True

    screen.fill('black')
    draw_board()
    draw_pacman()
    center_x = pacman_start_x + 23
    center_y = pacman_start_y + 24
    turns_allowed = check_position(center_x, center_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3


    pygame.display.flip()
pygame.quit()
