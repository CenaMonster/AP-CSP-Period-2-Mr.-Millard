#######################################################
# Brandon Le                                          #
# Description: A fighting game where you can jump and #
# attack. You are able to pick between multiple stages#
# There will be multiple characters.                  #
#######################################################

import pygame
from pygame import mixer
from fighter import Fighter

screen_width = 1000 #creates window
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Sidewalk Fisticuffs")   #titles window

clock = pygame.time.Clock()     #sets frames
FPS = 60

RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

MARTIALHERO_SIZE = 250
MARTIALHERO_SCALE = 3
MARTIALHERO_OFFSET = [105, 113]
MARTIALHERO_DATA = [MARTIALHERO_SIZE, MARTIALHERO_SCALE, MARTIALHERO_OFFSET]
MARTIALHERO2_SIZE = 250
MARTIALHERO2_SCALE = 3
MARTIALHERO2_OFFSET = [92, 120]
MARTIALHERO2_DATA = [MARTIALHERO2_SIZE, MARTIALHERO2_SCALE, MARTIALHERO2_OFFSET]

bg_image = pygame.image.load("fightingbg1.gif").convert_alpha() #loads bg into window

martialhero_sheet = pygame.image.load("Martial Hero/Sprites/Martial Hero 2.0.png").convert_alpha()  #loads spritesheets
martialhero2_sheet = pygame.image.load("Martial Hero 2/Sprites/Martial Hero 2 2.0.png").convert_alpha()


MARTIALHERO_ANIMATION_STEPS = [8, 8, 1, 6, 6, 4, 6]
MARTIALHERO2_ANIMATION_STEPS = [4, 8, 1, 4, 4, 3, 7]


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height)) #stretches bg into window
    screen.blit(scaled_bg, (0, 0))


def draw_health_bar(health, x , y):     #draw health bar
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


fighter_1 = Fighter(200, 310, False, MARTIALHERO_DATA, martialhero_sheet, MARTIALHERO_ANIMATION_STEPS)    #creates two instance of fighters
fighter_2 = Fighter(700, 390, True, MARTIALHERO2_DATA, martialhero2_sheet, MARTIALHERO2_ANIMATION_STEPS)


run = True  #loops game
while run:

    clock.tick(FPS)

    draw_bg()   #draws background

    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)


    fighter_1.move(screen_width, screen_height, screen, fighter_2)    #moves fighters
    #fighter_2.move()

    fighter_1.update()
    fighter_2.update()

    fighter_1.draw(screen) #draws fighters into window
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()