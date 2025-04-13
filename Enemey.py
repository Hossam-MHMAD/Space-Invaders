import random

class Enemy:

    def __init__(self, screen_width, enemies_dict):
        self.enemies_dict = enemies_dict
        self.screen_width = screen_width
        self.width = 70
        self.height = 50
        self.x = random.randint(0, screen_width - self.width)
        self.y = -50
        self.speed = 2
        self.image_type = random.choice(list(self.enemies_dict.keys())) # Will take an enemies_dict then choose Randomly from it! (from images)
        

    def Move(self): # Because If The an enemy is out of the screen so the player will lose a life
        self.y += self.speed

    def Draw(self, window): 
        window.blit(self.enemies_dict[self.image_type], (self.x, self.y))
