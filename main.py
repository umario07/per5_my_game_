# This file was created by: Umair Mughal


# IMPORT REQUIRED MODULES AND LIBRARIES
# pygame is used to make the game, settings, sprites, and tilemap are custom files, 
# path is used to handle file paths, randint gives us random numbers
import pygame as pg
from settings import *
from sprites import *
from tilemap import *
from os import path
from random import randint




'''
Elevator Pitch: an ariel view penalty shoutout with a moving goalkeeper

Goals: score a goal with a moving goalie
Rules: the ball spawns in a new place every time and you need to get 10 goals in 10 seconds with a moving goalkeeper. 
Feedback: goal scoring 
Freedom: left and right movement to find the ball

What's the sentence: You scored a goal! You win! Saved! You lost!


'''









# Game class will hold everything the game needs to work, like the player, enemies, and the map
class Game:
    # The __init__ function runs when the game starts
    # It sets up things like the screen, sound, and the clock that controls the game speed
    def __init__(self):
        pg.init()  # This starts pygame so we can use it
        pg.mixer.init()  # This starts the sound system
        # Create a game window with the WIDTH and HEIGHT from settings.py
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # Set the window title (what is written on the top of the window)
        pg.display.set_caption("Umair's Game")
        # This creates a clock to keep track of time in the game (controls frames per second)
        self.clock = pg.time.Clock()
        # 'running' will be True while the game is running, it stops the game when we want
        self.running = True

    # This function will load the game data (like the map)
    def load_data(self):
        # Get the path to the folder where this file is located
        self.game_folder = path.dirname(__file__)
        # Load the map from a text file (level1.txt)
        self.map = Map(path.join(self.game_folder, 'level1.txt'))

    # Start a new game, this creates all the objects we need like the player and enemies
    def new(self):
        # Load the map and other data when we start a new game
        self.load_data()
        # Print the map data (this is for testing, so we can see the map in the console)
        print(self.map.data)
        # Create groups for all sprites, walls, mobs (enemies), powerups, and coins
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()  # Added group for coins
        
        # Now we go through each row and column in the map data to place objects
        # 'enumerate' helps us know which row and column we are on
        for row, tiles in enumerate(self.map.data):
            # Print the row number (for testing)
            print(row)
            # Look at each tile (or character) in that row
            for col, tile in enumerate(tiles):
                # Print the column number (for testing)
                print(col)
                # If the tile is '1', create a wall at that position
                if tile == '1':
                    Wall(self, col, row)
                # If the tile is 'P', create the player at that position
                if tile == 'P':
                    self.player = Player(self, col, row)
                # If the tile is 'M', create a mob (enemy) at that position
                if tile == 'M':
                    Mob(self, col, row)
                # If the tile is 'U', create a powerup at that position
                if tile == 'U':
                    Powerup(self, col, row)
                # If the tile is 'C', create a coin at that position
                if tile == 'C':
                    Coin(self, col, row)  # Added code to create coins

    # This is the main loop that keeps the game running
    def run(self):
        # While the game is set to 'running', keep doing these things
        while self.running:
            # Get the time passed between frames (this helps with smooth movement)
            self.dt = self.clock.tick(FPS) / 1000
            # Check for events like key presses or closing the game
            # Check for player input or game events, like closing the window
            self.events()
            # Update the game (move characters, check collisions, etc.)
            self.update()
            # Draw everything on the screen
            self.draw()

    # Check for player input or game events, like closing the window
    def events(self):
        # This goes through all the events happening in the game
        for event in pg.event.get():
            # If the event is quitting the game (like clicking the 'X' button), stop running
            if event.type == pg.QUIT:
                self.running = False

    # Update all the sprites in the game, like the player and enemies
    def update(self):
        # Call the update method for all sprites in the game
        self.all_sprites.update()

    # Draw text on the screen (used for showing messages like the timer)
    def draw_text(self, surface, text, size, color, x, y):
        # Find the font that matches 'arial' (a type of text style)
        font_name = pg.font.match_font('arial')
        # Create the font with the chosen size
        font = pg.font.Font(font_name, size)
        # Render the text, which turns it into an image we can display
        text_surface = font.render(text, True, color)
        # Get the size of the text image so we can position it correctly
        text_rect = text_surface.get_rect()
        # Set the position of the text (x, y coordinates)
        text_rect.midtop = (x, y)
        # Draw the text on the screen
        surface.blit(text_surface, text_rect)

    # Draw everything on the screen each frame
    def draw(self):
        # Fill the screen with white (to clear it before drawing new things)
        self.screen.fill(WHITE)
        # Draw all the sprites (player, enemies, etc.) onto the screen
        self.all_sprites.draw(self.screen)
        # Draw the time (dt) in milliseconds at the top left of the screen
        # self.draw_text(self.screen, str(self.dt * 1000), 24, WHITE, WIDTH / 30, HEIGHT / 30)
        # Draw the number of coins collected by the player at the top center of the screen
        self.draw_text(self.screen, "Coins collected: " + str(self.player.coins), 24, BLACK, WIDTH / 2, HEIGHT / 24)  # Added coin display
        # Update the screen with everything we just drew
        pg.display.flip()

# If this file is run directly, create a Game object and start the game
if __name__ == "__main__":
    # Create an instance of the Game class (starts everything)
    g = Game()
    # Call the 'new' method to set up a new game
    g.new()
    # Call the 'run' method to start the game loop
    g.run()
