# This file was created by: Umair Mughal

# this is where we import libraries and modules
from random import randint
import pygame as pg
from settings import *
from sprites import *
from tilemap import *
from os import path 
# we are editing this file after installing git
# settings and sprites are custom modules that store game settings

# create a game class 
# its defined to manage the game 
class Game:
  def __init__(self):
    pg.init()
    self.clock = pg.time.Clock()
    # this creates a clock to control the games frame rate 
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    # sets the dimension of the game window to width and height, imported from settings
    self.playing = True
 
  def load_data(self):
    self.game_folder = path.dirname(__file__)
    # joining the game folder 
    self.map = Map(path.join(self.game_folder, 'leve1.txt'))
    # 

  # this is where the game creates the stuff you see and hear
  def new(self):
    self.load_data
    print(self.map.data)
    self.all_sprites = pg.sprite.Group()
    self.all_walls = pg.sprite.Group()
    self.all_mobs = pg.sprite.Group()
    self.all_powerups = pg.sprite.Group()
    # create sprite group using pygame 
    # sets up the game environment 
    self.all_sprites = pg.sprite.Group()
    self.all_walls = pg.sprite.Group()
    # these create groups to store sprite objects 
    # the class to create the player object 
   # self.player = Player(self, 5, 5)
    #self.mob = Mob(self, 100, 100)
    # makes new mobs using a for loop
    #self.wall = Wall(self, WIDTH//2, HEIGHT//2)
    # represent game objects like players, enemies, mobs 
    #for i in range(6):
      # this loop adds 6 wall and mob objects
      #Wall(self, i*TILESIZE, i*TILESIZE)
     # Mob(self, i*randint(0, 200), i*randint(0,200)) # instantiate mobs in random places
      #print(w.rect.x)
      #  prints the x-coordinate of each wall
    #  m = Mob(self, TILESIZE*i, TILESIZE*i)

    for row, tiles in enumerate(self.map.data):
      print(row)
      for col, tile in enumerate(tiles):
        #gives it column and tile value
        print(col)
        if tile =="1":
          #creates a wall out of the tile
          Wall(self, col, row)
          # uses x(col), y(row)
        if tile =="P":
          #creates a wall out of the tile
          Player(self, col, row)
          # uses x(col), y(row)
        if tile =="M":
          #creates a wall out of the tile
          Mob(self, col, row)
          # uses x(col), y(row)
        if tile == 'U':
                    Powerup(self, col, row)


# this is a method
# like functions that are part of a class
# the run method runs the game loop
  def run(self):
    while self.playing:
      self.dt = self.clock.tick(FPS) / 1000
      # makes sure the game runs at a consistent frame rate 
      # input
      self.events()
      # process
      # handles user inputs 
      self.update()
      # output
      # updates things that go on in the game 
      self.draw()
      # puts objects on the screen

    pg.quit()
  # input
  def events(self):
    for event in pg.event.get():
        if event.type == pg.QUIT:
          # if the player closes the game window, it sets to false and stops the game loop
          self.playing = False
  # process
  # checks for events 

  def update(self):
    # update all the sprites
    self.all_sprites.update()
    # updates are defined in sprites 


    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surface.blit(text_surface, text_rect)
  # output
  def draw(self):
    self.screen.fill((0, 0, 0))
    # clears the screen by filling it with black 
    # draws all the sprite objects
    self.all_sprites.draw(self.screen)
    # draws all the sprites
    pg.display.flip()
    # updates display to show the new frame

if __name__ == "__main__":
  # instantiate
  # sets up game and runs it with g.run 
  print("main is running...")
  g = Game()
  print("main is running...")
  g.new()
  g.run()
  # only runs if script is ran directly and not imported 