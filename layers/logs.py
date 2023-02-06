import pygame
pygame.init()

from layers.tiles.water import Water, HEIGHT, WIDTH
from layers.const import *


class Logs:
    
    def __init__(self):
        
        self.layers = 2
        self.surface = getSurface(self.layers)
        
        for j in range(self.layers):
            for i in range(GRIDWIDTH):
                self.surface.blit(Water().surface, (i*WIDTH, j*HEIGHT))
