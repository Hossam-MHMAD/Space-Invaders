import pygame
import time
from Player import *
from Enemey import *
from Bullet import *
pygame.font.init()

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
            "player" : pygame.transform.scale(pygame.image.load("assets/pixel_ship_yellow.png"), (50, 50)), # So Unfortunatly i will write it fixed to don't scale it each frame!!
            "enemies" : {
                "ship_green" : pygame.transform.scale(pygame.image.load("assets/pixel_ship_green_small.png"), (70, 50)),
                "ship_red" : pygame.transform.scale(pygame.image.load("assets/pixel_ship_red_small.png"), (70, 50)),
                "ship_blue" : pygame.transform.scale(pygame.image.load("assets/pixel_ship_blue_small.png"), (50, 50))
            },
            "player_bullet" : pygame.transform.scale(pygame.image.load("assets/pixel_laser_yellow.png"), (50, 50)),
            "anemies_bullet" : pygame.transform.scale(pygame.image.load("assets/pixel_laser_red.png"), (50, 50))
        }
        self.Font = pygame.font.SysFont("verdana", 30)

        # Game Attributes
        self.enemies_list = []
        self.game_level = 1 # Current Level
        self.levels = 5 # Total Levels
        self.player = Player(self.WIDTH, self.HEIGHT)

        # Enemies Time 
        self.start_time = time.time()
        self.elapsed_time = 0

        # Time Should Pass 
        self.generate_time = self.levels * 1000 # This is the time to generate a new 3 enemies, because there'are 5 levels each Level The Player Should Kill 20 enemies but in difference generate time

    # Render On Screen
    def Render(self):
        self.WIN.blit(self.Assets["BG"], (0, 0)) # Render Background Img

        for enemy in self.enemies_list: # Draw Enemies
            enemy.Draw(self.WIN)

        self.player.Draw(self.WIN, self.Assets["player"]) # Draw The Player Shape

        # Render Text
        level_text = self.Font.render(f"Level: {self.game_level}", 1, "white")
        lives_text = self.Font.render(f"Lives: {self.player.lives}", 1, "white")

        self.WIN.blit(level_text, (self.WIDTH - level_text.get_width() - 10, 10))
        self.WIN.blit(lives_text, (10, 10))

        for bullet in self.player.bullets:
            self.WIN.blit(bullet.bullet_color, (bullet.x, bullet.y))

        pygame.display.update()

    def Generate_Enemies(self): # This Function To Generate 2 Enemies in each level time 
        if self.elapsed_time >= 300 and self.elapsed_time <= 310:
            enemy = Enemy(self.WIDTH, self.Assets["enemies"]) # Give Him A enemies dictionary to choose image
            self.enemies_list.append(enemy)

        # if self.elapsed_time >= 600 and self.elapsed_time <= 610:
        #     enemy = Enemy(self.WIDTH, self.Assets["enemies"]) # Give Him A enemies dictionary to choose image
        #     self.enemies_list.append(enemy)

        if self.elapsed_time > self.generate_time:

            enemy = Enemy(self.WIDTH, self.Assets["enemies"]) # Give Him A enemies dictionary to choose image
            
            self.elapsed_time = 0
        
            self.enemies_list.append(enemy)

    def Update(self):
        self.player.Move()

        self.Generate_Enemies()

        for enemy in self.enemies_list: # Move Enemies Down and check if one of them is out of the screen
            enemy.Move()
            if enemy.y > self.HEIGHT:
                self.player.lives -= 1
                self.enemies_list.remove(enemy)
            
        for bullet in self.player.bullets:
            bullet.Move_Up()
            if bullet.y > self.HEIGHT:
                self.player.bullets.remove(bullet)


    def Event_Handling(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL:
                    player_bullet = Bullet(self.player.x, self.player.y, self.Assets["player_bullet"])
                    self.player.bullets.append(player_bullet)

        return True


    def Run(self):
        while True:

            self.elapsed_time += self.clock.tick(60) # Set FPS AND Add TO elapsed_time

            run = self.Event_Handling() # Check If User Want to Quit

            if not run:
                break

            self.Update()
            self.Render()
        
        pygame.quit()


if __name__ == "__main__":
    Game().Run()

