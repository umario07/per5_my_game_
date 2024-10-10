# This file was created by: Umair Mughal
# This file was created by: Umair Mughal

# Importing the necessary libraries and modules
# pygame is used for game development, Sprite is a pygame class for game objects
# settings holds game settings, random is for generating random numbers
import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random

# The Player class defines the player character and its behavior
class Player(Sprite):
    # This function is called when a new player is created
    # x and y are the starting positions of the player
    def __init__(self, game, x, y):
        self.game = game  # Store reference to the main game
        # Add player to all_sprites group (so it can be updated and drawn)
        self.groups = game.all_sprites
        # Initialize the Sprite class with the groups
        Sprite.__init__(self, self.groups)
        # Create a surface (image) for the player that's 32x32 pixels
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()  # Get the rectangle of the image (used for positioning)
        self.image.fill(RED)  # Fill the player with a red color
        # Set player's position based on x and y coordinates, multiplying by tile size to place it on the grid
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10  # Set player's speed
        self.vx, self.vy = 0, 0  # Velocity (movement) in the x and y directions
        self.coins = 0  # Added missing coins attribute
        self.health = 100  # Added missing health attribute
    
    # This function checks which keys are pressed and moves the player accordingly
    def get_keys(self):
        # Get all keys that are currently pressed
        keys = pg.key.get_pressed()
        # Move up if 'w' is pressed
        if keys[pg.K_w]:
            self.vy -= self.speed
        # Move left if 'a' is pressed
        if keys[pg.K_a]:
            self.vx -= self.speed
        # Move down if 's' is pressed
        if keys[pg.K_s]:
            self.vy += self.speed
        # Move right if 'd' is pressed
        if keys[pg.K_d]:
            self.vx += self.speed
    
    # This function checks if the player is colliding with any walls
    def collide_with_walls(self, dir):
        # If checking for collisions in the x direction
        if dir == 'x':
            # Check if the player collides with any wall
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            # If a collision happened
            if hits:
                # If moving right, place the player to the left of the wall
                if self.vx > 0:
                    self.x = hits[0].rect.left - TILESIZE
                # If moving left, place the player to the right of the wall
                if self.vx < 0:
                    self.x = hits[0].rect.right
                # Stop the player's movement in the x direction
                self.vx = 0
                # Update the player's position
                self.rect.x = self.x
        # If checking for collisions in the y direction
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                # If moving down, place the player above the wall
                if self.vy > 0:
                    self.y = hits[0].rect.top - TILESIZE
                # If moving up, place the player below the wall
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                # Stop the player's movement in the y direction
                self.vy = 0
                # Update the player's position
                self.rect.y = self.y

    # This function checks if the player collides with other objects, like powerups
    def collide_with_stuff(self, group, kill):
        # Check for collisions with any object in the specified group
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            # If the player hits a powerup, print a message
            if str(hits[0].__class__.__name__) == "Powerup":
                print("I hit a powerup...")
            # If the player hits a coin, increase the coin count
            if str(hits[0].__class__.__name__) == "Coin":
                print("I hit a coin...")
                self.coins += 1  # Added missing coin logic

    # This function updates the player's position and checks for collisions
    def update(self):
        self.get_keys()  # Check for key presses to move the player
        # Update player's position based on velocity and time
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        # Check if the player collects any powerups or coins
        self.collide_with_stuff(self.game.all_powerups, True)
        self.collide_with_stuff(self.game.all_coins, True)  # Added missing coin collision

        # Update the player's rectangle position and check for wall collisions
        self.rect.x = self.x
        self.collide_with_walls('x')

        self.rect.y = self.y
        self.collide_with_walls('y')

# The Mob class defines enemies or other moving objects
class Mob(Sprite):
    # This function is called when a new mob is created
    def __init__(self, game, x, y):
        self.game = game  # Store reference to the main game
        # Add mob to all_sprites group
        self.groups = game.all_sprites
        # Initialize the Sprite class with the groups
        Sprite.__init__(self, self.groups)
        # Create a surface (image) for the mob that's 32x32 pixels
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()  # Get the rectangle of the image (used for positioning)
        self.image.fill(GREEN)  # Fill the mob with a green color
        # Set mob's position based on x and y coordinates
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 10  # Set mob's speed
        # Randomly assign a category (this can be used for different mob types)
        self.category = random.choice([0, 1])
    
    # This function updates the mob's position and behavior
    def update(self):
        # Move the mob horizontally (side to side)
        self.rect.x += self.speed

        # Check if the mob hits any walls
        hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
        # If the mob hits a wall, reverse direction and move down
        if hits:
            self.speed *= -1
            self.rect.y += 32  # Move down 32 pixels (one tile)
        
        # If the mob goes off the screen, reverse direction and move down
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed *= -1
            self.rect.y += 32


# The Wall class defines solid objects the player and mobs cannot pass through
class Wall(Sprite):
    # This function is called when a new wall is created
    def __init__(self, game, x, y):
        self.game = game  # Store reference to the main game
        # Add wall to all_sprites and all_walls groups
        self.groups = game.all_sprites, game.all_walls
        # Initialize the Sprite class with the groups
        Sprite.__init__(self, self.groups)
        # Create a surface (image) for the wall that's the size of one tile
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()  # Get the rectangle of the image (used for positioning)
        self.image.fill(BLUE)  # Fill the wall with a blue color
        # Set wall's position based on x and y coordinates
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    # Walls don't move, so we don't need to update them
    def update(self):
        pass


# The Powerup class defines items the player can collect
class Powerup(Sprite):
    # This function is called when a new powerup is created
    def __init__(self, game, x, y):
        self.game = game  # Store reference to the main game
        # Add powerup to all_sprites and all_powerups groups
        self.groups = game.all_sprites, game.all_powerups
        # Initialize the Sprite class with the groups
        Sprite.__init__(self, self.groups)
        # Create a surface (image) for the powerup that's the size of one tile
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()  # Get the rectangle of the image (used for positioning)
        self.image.fill(PINK)  # Fill the powerup with a pink color
        # Set powerup's position based on x and y coordinates
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Coin(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_coins
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE