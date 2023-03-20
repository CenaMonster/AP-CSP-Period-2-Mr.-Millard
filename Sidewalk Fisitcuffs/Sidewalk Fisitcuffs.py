#######################################################
# Brandon Le                                          #
# Description: A fighting game where you can jump and #
# attack. You are able to pick between multiple stages#
# There will be multiple characters.                  #
#######################################################

import pygame
from fighter import Fighter

screen_width = 1280 #creates window
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Sidewalk Fisticuffs")   #titles window

clock = pygame.time.Clock()     #sets frames
FPS = 60

RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

bg_image = pygame.image.load("fightingbg1.gif").convert_alpha() #loads bg into window

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height)) #stretches bg into window
    screen.blit(scaled_bg, (0, 0))


def draw_health_bar(health, x , y):     #draw health bar
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 504, 34))
    pygame.draw.rect(screen, RED, (x, y, 500, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 500 * ratio, 30))


fighter_1 = Fighter(200,510)    #creates two instance of fighters
fighter_2 = Fighter(1000,510)


run = True  #loops game
while run:

    clock.tick(FPS)

    draw_bg()   #draws background

    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 760, 20)


    fighter_1.move(screen_width, screen_height, screen, fighter_2)    #moves fighters
    #fighter_2.move()

    fighter_1.draw(screen) #draws fighters into window
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()