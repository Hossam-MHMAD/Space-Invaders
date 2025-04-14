
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
        self.wait = True
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
        self.Win_Lose_Font = pygame.font.SysFont("verdana", 100)
        self.Wait_Font = pygame.font.SysFont("verdana", 50)

        # Game Attributes
        self.enemies_list = []
        self.enemies_bullets = [] # list of bullet objects 
        self.game_level = 1 # Current Level
        self.levels = 5 # Total Levels
        self.player = Player(self.WIDTH, self.HEIGHT)

        # Enemies Time 
        self.start_time = time.time()
        self.elapsed_time = 0

        # Time Should Pass 
        self.generate_time = self.levels * 1000 # This is the time to generate a new 2 enemies, because there'are 5 levels each Level The Player Should Kill 20 enemies but in difference generate time

    # Render On Screen
    def Render(self):
        self.WIN.blit(self.Assets["BG"], (0, 0)) # Render Background Img
        
        if self.wait:
            wait_txt = self.Wait_Font.render("Press Any Key To Start!", 1, "white")
            self.WIN.blit(wait_txt, (self.WIDTH/2 - wait_txt.get_width()/2, self.HEIGHT/2 - wait_txt.get_height()/2))
            pygame.display.update()
            return

        for enemy in self.enemies_list: # Draw Enemies
            enemy.Draw(self.WIN)

        self.player.Draw(self.WIN, self.Assets["player"]) # Draw The Player Shape

        # Render Text
        level_text = self.Font.render(f"Level: {self.game_level}", 1, "white")
        lives_text = self.Font.render(f"Lives: {self.player.lives}", 1, "white")
        kills_text = self.Font.render(f"Kills: {self.player.kill}", 1, "white")

        self.WIN.blit(level_text, (self.WIDTH - level_text.get_width() - 10, 10))
        self.WIN.blit(lives_text, (10, 10))
        self.WIN.blit(kills_text, (self.WIDTH/2 - kills_text.get_width()/2, 10))


        for enemy_bullet in self.enemies_bullets:
            self.WIN.blit(enemy_bullet.bullet_color, (enemy_bullet.x, enemy_bullet.y))


        for bullet in self.player.bullets:
            self.WIN.blit(bullet.bullet_color, (bullet.x, bullet.y))

        pygame.display.update()

    def Generate_Enemies(self): # This Function To Generate 2 Enemies in difference time to don't be collided  
        if self.elapsed_time >= 300 and self.elapsed_time <= 310:
            enemy = Enemy(self.WIDTH, self.Assets["enemies"]) # Give Him A enemies dictionary to choose image
            self.enemies_list.append(enemy)

        if self.elapsed_time > self.generate_time:

            enemy = Enemy(self.WIDTH, self.Assets["enemies"]) # Give Him A enemies dictionary to choose image

            self.elapsed_time = 0
        
            self.enemies_list.append(enemy)

    def Update(self):

        #Player Movement 
        self.player.Move()

        self.Generate_Enemies()

        # Move Enemies Down and check if one of them is out of the screen
        for enemy in self.enemies_list: 
            enemy.Move()
            if enemy.y > self.HEIGHT:
                self.player.lives -= 1
                self.enemies_list.remove(enemy)
            
        # Move Player Bullets Up
        for bullet in self.player.bullets: 
            bullet.Move_Up()
            if bullet.y > self.HEIGHT:
                self.player.bullets.remove(bullet)

        # Check If Player Bullet Is Collided with an enemy
        for bullet in self.player.bullets: 
            for enemy in self.enemies_list:
                if pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height).colliderect(pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)):
                    self.player.kill += 1  
                    self.player.track_kills += 1
                    self.enemies_list.remove(enemy)
                    self.player.bullets.remove(bullet)
                    break

        for enemy_bullet in self.enemies_bullets:
            if pygame.Rect(enemy_bullet.x, enemy_bullet.y, enemy_bullet.width, enemy_bullet.height).colliderect(pygame.Rect(self.player.x, self.player.y, self.player.player_width, self.player.player_height)):
                self.enemies_bullets.remove(enemy_bullet)
                self.player.health -= 10

        # Make the enemies shoot
        for enemy in self.enemies_list: 
            enemy.Shoot(self.enemies_bullets, self.Assets["anemies_bullet"])

        # Make enemies Bullets Move
        for enemy_bullet in self.enemies_bullets:  
            enemy_bullet.y += 5 #  Bullet SPeed
            if enemy_bullet.y > self.HEIGHT:
                self.enemies_bullets.remove(enemy_bullet)

        # Check 100 Kill if yes so win
        if self.player.kill == 100:
            win_text = self.Win_Lose_Font.render("YOU WIN", 1, "white")
            self.WIN.blit(win_text, (self.WIDTH/2 - win_text.get_width()/2, self.HEIGHT/2 - win_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            return True
        
        # Check Lose
        if self.player.lives == 0 or self.player.health == 0:
            win_text = self.Win_Lose_Font.render("YOU Lose", 1, "white")
            self.WIN.blit(win_text, (self.WIDTH/2 - win_text.get_width()/2, self.HEIGHT/2 - win_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            return True

        # Level Up When player kill 20 enimies
        if self.player.track_kills > 19:
            self.game_level += 1
            self.levels -= 1
            self.generate_time = self.levels * 1000
            self.player.track_kills = 0

    def Event_Handling(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                self.wait = False
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

            if not self.wait:
                done = self.Update()
                if done:
                    break
            self.Render()


        
        pygame.quit()


if __name__ == "__main__":
    Game().Run()

