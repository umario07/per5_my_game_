# This file was created by: Umair Mughal

import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random

class Player(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        # Create a 32x32 surface for the player and set its position
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)  # Fill the player with red color
        self.x = x * TILESIZE  # Adjust position based on tile size
        self.y = y * TILESIZE
        self.speed = 10  # Player movement speed
        self.vx, self.vy = 0, 0  # Velocity for x and y direction
        
    def get_keys(self):
        # Handle key presses for movement
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:  # Move up
            self.vy -= self.speed
        if keys[pg.K_a]:  # Move left
            self.vx -= self.speed
        if keys[pg.K_s]:  # Move down
            self.vy += self.speed
        if keys[pg.K_d]:  # Move right
            self.vx += self.speed
            
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    #coming from left side
                    self.x = hits[0].rect.left - self.rect.width 
                    # makes it so that the proper part of the object hits the proper part of the wall 
                
                if self.vx < 0:
                    # coming from right side
                    self.x = hits[0].rect.right
                    # no - because it is gonna hit the right side already
                self.vx = 0
                self.rect.x = self.x
        
        # same thing but for top and bottom 
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        # Get the movement input and apply it to the player's position
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        # Update player's rectangle position based on movement
        self.rect.x = self.x
        self.rect.y = self.y

class Mob(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        # Create a 32x32 surface for the mob and place it on the screen
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)  # Fill the mob with green color
        self.rect.x = x
        self.rect.y = y
        self.speed = 10  # Mob movement speed
        self.category = random.choice([0,1])  # Random category for some future use (maybe)
        
    def update(self):
        # Move the mob horizontally
        self.rect.x += self.speed
        
        # Reverse direction when hitting the sides of the screen and move down
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed *= -1  # Change direction
            self.rect.y += 32  # Move down one tile
     
        # moving towards the side of the screen
        self.rect.x += self.speed
        # when it hits the side of the screen, it will move down
        if self.rect.right > WIDTH or self.rect.left < 0:
            # print("off the screen...")
            self.speed *= -1
            self.rect.y += 32
        # elif self.rect.colliderect(self.game.player):
        #     self.speed *= -1
        # elif self.rect.colliderect(self):
        #     self.speed *= -1
        # Placeholder for collision checks, maybe with player or another mob
        # Future collision 

class Wall(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        # Create a wall block of TILESIZE and position it on the grid
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)  # Fill the wall with blue color
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        # Walls don't need to update, they just exist as barriers
        pass

    class Powerup(Sprite):
        def __init__(self, game, x, y):
            self.game = game
            self.groups = game.all_sprites, game.all_powerups
            Sprite.__init__(self, self.groups)
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.rect = self.image.get_rect()
            self.image.fill(PINK)
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE