import pygame

class Player:
    def __init__(self, window_width, window_height): # Take Window w,h to determine player x and y
        # Player Init
        self.player_width = 50
        self.player_height = 50
        self.x = window_width / 2 - self.player_width / 2
        self.y = window_height - self.player_height # Should Add More space for the health bar!!
        self.health = 100
        self.speed = 10
        self.lives = 5
        self.bullets = []

        
    def Draw(self, window, player_img):
        player = pygame.transform.scale(player_img, (self.player_width, self.player_height))

        window.blit(player, (self.x, self.y))

