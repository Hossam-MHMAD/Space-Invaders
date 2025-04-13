import pygame
from HealthBar import *

class Player:
    def __init__(self, window_width, window_height): # Take Window w,h to determine player x and y
        # Player Init
        self.screen_width = window_width
        self.screen_height = window_height
        self.player_width = 50
        self.player_height = 50
        self.x = window_width / 2 - self.player_width / 2
        self.y = window_height - self.player_height - 15 # 15 -> 10 for health_bar and 5 extra space
        self.health = 100
        self.speed = 5  
        self.lives = 5
        self.bullets = [] # Will Store The Player Bullets when he shoot
        self.kill = 0 # Each 20 Kill Level Up

        # Health Bar
        self.health_bar = HealthBar()

    def Draw(self, window, player_img):
        # player = pygame.transform.scale(player_img, (self.player_width, self.player_height)) -> To Don't Scale Each Frame!!
        window.blit(player_img, (self.x, self.y))
        self.health_bar.Draw(window, self.health, self.x, self.y + self.player_height)

    def Move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.player_height + 15 < self.screen_height:
            self.y += self.speed
        if keys[pygame.K_RIGHT] and self.x + self.player_width < self.screen_width:
            self.x += self.speed
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed

    # def Shoot(self):


