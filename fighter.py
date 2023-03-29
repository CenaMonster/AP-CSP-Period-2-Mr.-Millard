import pygame

class Fighter():
    def __init__(self, x , y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:idle #1:run #2:jump #3:attack1 #4:attack2 #5:hit #6:death  
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        print(animation_list)
        return animation_list

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



    def update(self):   #animation updates
        animation_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]     #update image
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:     #checks to see if the correct amount of time has passed since update
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()  
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0 

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10



        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (250, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))