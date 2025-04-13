import pygame

class HealthBar:
    def __init__(self):
        self.width = 50
        self.height = 5
        self.max_health = 100
    
    def Draw(self, window, player_health, x, y):
        green_health = player_health / self.max_health
        pygame.draw.rect(window, "red", pygame.Rect(x, y, self.width, self.height))
        pygame.draw.rect(window, "green", pygame.Rect(x, y, self.width * green_health, self.height))