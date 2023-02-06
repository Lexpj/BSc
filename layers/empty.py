import pygame
pygame.init()

from layers.tiles.grass import Grass, HEIGHT, WIDTH
from layers.const import *


class Empty:
    
    def __init__(self):
        
        self.layers = 1
        self.surface = getSurface(self.layers)
        
        
        for i in range(GRIDWIDTH):
            self.surface.blit(Grass().surface, (i*WIDTH, 0))
    