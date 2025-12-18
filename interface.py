import pygame
from pygame import FULLSCREEN
from boards_for_levels import boards
import math
pygame.init()

WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN ) # FULLSCREEN???
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 32)
level1 = boards
color_for_walls = 'blue'
color_for_food = 'white'
PI = math.pi

pacman_images = []
for i in range(1,5):
    pacman_images.append(pygame.transform.scale(pygame.image.load(f'assets/pacman_images/{i}.png'), (45, 45)))

blinky_image = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'), (45, 45))
pinky_image = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/pink.png'), (45, 45))
inky_image = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/blue.png'), (45, 45))
clyde_image = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/orange.png'), (45, 45))
dead_image = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/dead.png'), (45, 45))
spooked_image = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/powerup.png'), (45, 45))

pacman_x = 450 # IT`S A TOP LEFT CORNER
pacman_y = 663
direction = 0

blinky_x = 56
blinky_y = 58
blinky_direction = 0

pinky_x = 440
pinky_y = 438
pinky_direction = 2

inky_x = 440
inky_y = 438
inky_direction = 2

clyde_x = 440
clyde_y = 438
clyde_direction = 2

direction_command = 0
counter = 0
flicker = False
turns_allowed = [False, False, False, False]
pacman_speed =  2
score = 0
powerup = False
power_counter = 0
eaten_ghost = [False, False, False, False]
targets = [(pacman_x, pacman_y), (pacman_x, pacman_y), (pacman_x, pacman_y), (pacman_x, pacman_y)]

blinky_dead = False
pinky_dead = False
inky_dead = False
clyde_dead = False

blinky_box = False
pinky_box = False
inky_box = False
clyde_box = False

ghost_speed = 2

startup_counter = 0
lives = 3

class Ghost:
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 22
        self.center_y = self.y_pos + 22
        self.target = target
        self.speed = speed
        self.img = img
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()

    def draw(self):
        if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
            screen.blit(self.img, (self.x_pos, self.y_pos))
        elif powerup and not self.dead and not eaten_ghost[self.id]:
            screen.blit(spooked_image, (self.x_pos, self.y_pos))
        else:
            screen.blit(dead_image, (self.x_pos, self.y_pos))
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36,36))
        return ghost_rect

    def check_collisions(self):
        pass
        return self.turns, self.in_box

def draw_misc():
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (10, 920))
    if powerup:
        pygame.draw.circle(screen, 'blue', (140, 930), 15)
    for i in range(lives):
        screen.blit(pygame.transform.scale(pacman_images[0], (30, 30)), (650 + i * 40, 915))

def check_collisions(scor, power, power_count, eaten_ghosts):
    num1 = (HEIGHT - 50) // 32
    num2 = WIDTH // 30
    if 0 < pacman_x < 870:
        if level1[center_y // num1][center_x // num2] == 1:
            level1[center_y // num1][center_x // num2] = 0
            scor += 10
        if level1[center_y // num1][center_x // num2] == 2:
            level1[center_y // num1][center_x // num2] = 0
            scor += 50
            power = True
            power_count = 0
            eaten_ghosts = [False, False, False, False]

    return scor, power, power_count, eaten_ghosts

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
        screen.blit(pacman_images[counter // 5], (pacman_x, pacman_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(pacman_images[counter // 5],True, False),
                    (pacman_x, pacman_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 5], 90), (pacman_x, pacman_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 5], -90), (pacman_x, pacman_y))

def check_turns(centerx, centery):
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

def move_pacman(pacm_x, pacm_y):
    if direction == 0 and turns_allowed[0]:
        pacm_x += pacman_speed
    elif direction == 1 and turns_allowed[1]:
        pacm_x -= pacman_speed
    if direction == 2 and turns_allowed[2]:
        pacm_y -= pacman_speed
    elif direction == 3 and turns_allowed[3]:
        pacm_y += pacman_speed
    return pacm_x, pacm_y

# def draw_blinky():
#     if blinky_direction == 0:
#         screen.blit(blinky_image, (blinky_x, blinky_y))
#     elif blinky_direction == 1:
#         screen.blit(pygame.transform.flip(blinky_image, True, False), (blinky_x, blinky_y))
#     elif blinky_direction == 2:
#         screen.blit(pygame.transform.rotate(blinky_image, 90), (blinky_x, blinky_y))
#     elif blinky_direction == 3:
#         screen.blit(pygame.transform.rotate(blinky_image, -90), (blinky_x, blinky_y))




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
    if powerup and power_counter < 600:
        power_counter +=1
    elif powerup and power_counter >= 600:
        power_counter = 0
        powerup = False
        eaten_ghost = [False, False, False, False]
    if startup_counter < 180:
        moving = False
        startup_counter +=1
    else:
        moving = True

    screen.fill('black')
    draw_board()
    draw_pacman()
    # draw_blinky()
    draw_misc()
    center_x = pacman_x + 23
    center_y = pacman_y + 24
    turns_allowed = check_turns(center_x, center_y)
    if moving:
        pacman_x, pacman_y = move_pacman(pacman_x, pacman_y)
    score, powerup, power_counter, eaten_ghost = check_collisions(score, powerup, power_counter, eaten_ghost)


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
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT and direction_command == 0:
        #         direction_command = direction
        #     if event.key == pygame.K_LEFT and direction_command == 1:
        #         direction_command = direction
        #     if event.key == pygame.K_UP and direction_command == 2:
        #         direction_command = direction
        #     if event.key == pygame.K_DOWN and direction_command == 3:
        #         direction_command = direction

        #  BETTER  NOT  TO ERASE, IT MAY BE CORRECT

    if direction_command == 0 and turns_allowed[0]:
        direction = 0
    if direction_command == 1 and turns_allowed[1]:
        direction = 1
    if direction_command == 2 and turns_allowed[2]:
        direction = 2
    if direction_command == 3 and turns_allowed[3]:
        direction = 3
    if pacman_x > 900:
        pacman_x = -47
    elif pacman_x < -50:
        pacman_x = 897
    pygame.display.flip()
pygame.quit()
