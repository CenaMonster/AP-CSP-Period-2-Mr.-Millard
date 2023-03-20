import pygame

class Fighter():
    def __init__(self, x ,y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()  #gets key presses

        if self.attacking == False:

            if key[pygame.K_a]:     #movement
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            if key[pygame.K_w] and self.jump == False:  #jump
                self.vel_y = -30
                self.jump = True
            if key[pygame.K_u] or key[pygame.K_o]:     #attacks
                self.attack(surface, target)

                if key[pygame.K_u]:
                    self.attack_type = 1
                if key[pygame.K_o]:
                    self.attack_type = 1


        self.vel_y += GRAVITY   #applies gravity
        dy += self.vel_y    



        if self.rect.left + dx < 0:     #makes it so player stays on screen
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 30:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 30 - self.rect.bottom


        if target.rect.centerx > self.rect.centerx:      #makes it so players are faced towards each other
            self.flip = False
        else:
            self.flip = True 


        self.rect.x += dx     #update player movement
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10



        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
    def draw(self, surface):
        pygame.draw.rect(surface, (250, 0, 0), self.rect)