import pygame as pg 
from settings import*

class map:
    def __init__(self, filename):
    # it initalizes the file
        self.data = []
        #list
        with open(filename, 'rt') as f:
        # gives python the power to open filenames 
        # different arguments to put in there
            for line in f: 
            # for loop
                self.data.append(line.strip()) # <- anything not a number, we get rid of it (line.strip)
                # taking the empty list and putting stuff in it - what append does 
        self.tilewidth = len(self.data[0])
        # the length of the entire level is equal the the length of level 0
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE