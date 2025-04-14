class Bullet:
  def __init__(self,x , y, player_img = None):
    self.x = x
    self.y = y
    self.width = 20
    self.height = 30
    self.speed = 5
    self.bullet_color = player_img

  def Move_Up(self):
    self.y -= self.speed

  def Move_Down(self):
    self.y += self.speed
