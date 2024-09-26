# This file was created by: Umair Mughal

# this is where we import libraries and modules
import pygame as pg
from settings import *
from sprites import *
# we are editing this file after installing git

# create a game class 
class Game:
  def __init__(self):
    pg.init()
    self.clock = pg.time.Clock()
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    self.playing = True
  # this is where the game creates the stuff you see and hear
  def new(self):
    # create sprite group using pygame 
    self.all_sprites = pg.sprite.Group()
    self.all_walls = pg.sprite.Group()
    # the class to create the player object 
    self.player = Player(self, 5, 5)
    self.mob = Mob(self, 100, 100)
    self.wall = Wall(self, WIDTH//2, HEIGHT//2)

    for i in range(6):
      w = Wall(self, TILESIZE*i, TILESIZE*i)
      print(w.rect.x)
      m = Mob(self, TILESIZE*i, TILESIZE*i)

# this is a method
# like functions that are part of a class
# the run method runs the game loop
  def run(self):
    while self.playing:
      self.dt = self.clock.tick(FPS) / 1000
      # input
      self.events()
      # process
      self.update()
      # output
      self.draw()

    pg.quit()
  # input
  def events(self):
    for event in pg.event.get():
        if event.type == pg.QUIT:
          self.playing = False
  # process
  # this is where the game updates the game state
  def update(self):
    # update all the sprites
    self.all_sprites.update()

  # output
  def draw(self):
    self.screen.fill((0, 0, 0))
    self.all_sprites.draw(self.screen)
    pg.display.flip()

if __name__ == "__main__":
  # instantiate
  print("main is running...")
  g = Game()
  print("main is running...")
  g.new()
  g.run()
  