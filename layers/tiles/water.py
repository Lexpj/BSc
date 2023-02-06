import pygame
pygame.init()

from layers.tiles.const import *


class Water:
    # Empty tile
    
    def __init__(self):
        
        # BASIC SETUP
        self.surface = pygame.image.load("./layers/tiles/assets/water.png")
        self.surface = pygame.transform.scale(self.surface, (WIDTH,HEIGHT))
        
        # ATTRIBUTES
        self.walkable = True