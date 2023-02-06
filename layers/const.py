import pygame
pygame.init()

from layers.tiles.const import *

# Width of a single layer

GRIDWIDTH = 15


# Simple function to generate a basis:
def getSurface(layers = 1):
    s = pygame.Surface((GRIDWIDTH*WIDTH,HEIGHT*layers))
    s = s.convert_alpha()
    s.fill((0, 0, 0, 0))
    return s