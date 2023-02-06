import pygame
pygame.init()

from layers.tiles.const import *


class Grass:
    # Empty tile
    
    def __init__(self):
        
        # BASIC SETUP
        self.surface = pygame.image.load("./layers/tiles/assets/grass.png")
        self.surface = pygame.transform.scale(self.surface, (WIDTH,HEIGHT))
        
        # ATTRIBUTES
        self.walkable = True