import random
import pygame
from Bullet import *

class Enemy:

    def __init__(self, screen_width, enemies_dict):
        self.enemies_dict = enemies_dict
        self.screen_width = screen_width
        self.width = 35
        self.height = 30
        # self.x = random.randint(0, screen_width - self.width)  this is the regtangle width i want it to be the image width which is 70
        self.x = random.randint(0, screen_width - 70) # 
        self.y = -50
        self.speed = 2
        self.image_type = random.choice(list(self.enemies_dict.keys())) # Will take an enemies_dict then choose Randomly from it! (from images)
        
        self.last_shoot_time = 0
        self.shooting_delay_time = random.randint(2000, 4000)  # Make The Soot delay random some enemies will shoot after 2se and other after 3 and so on

    def Move(self): # Because If The an enemy is out of the screen so the player will lose a life
        self.y += self.speed

    def Draw(self, window): 
        window.blit(self.enemies_dict[self.image_type], (self.x, self.y))

    def Shoot(self, enimies_bullets, bullet_img):
        current_time =  pygame.time.get_ticks()
        if current_time - self.last_shoot_time > self.shooting_delay_time:
            enimies_bullets.append(Bullet(self.x, self.y, bullet_img))
            self.last_shoot_time = current_time
