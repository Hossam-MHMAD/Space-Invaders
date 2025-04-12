import pygame
from Player import *

class Game:
    def __init__(self):
        # Window Init
        self.WIDTH = 600
        self.HEIGHT = 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Space Invaders")
        
        # Load Assets
        self.Assets = {
            "BG" : pygame.transform.scale(pygame.image.load("assets/background-black.png"), (self.WIDTH, self.HEIGHT)),
            "player" : pygame.image.load("assets/pixel_ship_yellow.png")
        }

        # Game Attributes
        self.enemies_list = []
        self.game_level = 1
        self.player = Player(self.WIDTH, self.HEIGHT)

    # Render On Screen
    def Render(self):
        self.WIN.blit(self.Assets["BG"], (0, 0)) # Render Background Img

        self.player.Draw(self.WIN, self.Assets["player"])

        pygame.display.update()

    def Event_Handling(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True


    def Run(self):
        while True:

            self.clock.tick(60) # Set FPS

            run = self.Event_Handling() # Check If User Want to Quit

            if not run:
                break

            self.Render()
        
        pygame.quit()


if __name__ == "__main__":
    Game().Run()

