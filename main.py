import pygame
from random import randint

from camera import Camera
from layers.empty import Empty
from layers.logs import Logs
from layers.tiles.const import HEIGHT, WIDTH

class World:
    
    def __init__(self):
        self.world = []
        self.surface = pygame.Surface((App.WIDTH,0))
        self.surface = self.surface.convert_alpha()
        self.surface.fill((0, 0, 0, 0))
        
    def draw(self):
        nrLayers = sum(layer.layers for layer in self.world)
        s = pygame.Surface((App.WIDTH,nrLayers*HEIGHT))
        s = s.convert_alpha()
        s.fill((0, 0, 0, 0))
        for i, layer in enumerate(self.world):
            s.blit(layer.surface, ((0, nrLayers*HEIGHT - ((i+layer.layers)*HEIGHT))))
        return s
    
    def __add__(self, val2):
        self.world.append(val2)
        self.surface = self.draw()
        return self
    

    
class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        App.WIDTH = 750
        App.HEIGHT = 700
        App.screen = pygame.display.set_mode((App.WIDTH, App.HEIGHT))
        App.clock = pygame.time.Clock()

        App.running = True
        App.environment = World()
        
        App.environment += Empty()
        App.environment += Logs()
        
        App.camera = Camera()
        


    def run(self):
        """Run the main event loop."""

        while App.running:

            # Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    App.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        App.camera.newy += 20
                    if event.key == pygame.K_a:
                        App.camera.newx += 20
                    if event.key == pygame.K_s:
                        App.camera.newy -= 20
                    if event.key == pygame.K_d:
                        App.camera.newx -= 20


            App.camera.update()
            
            # Draw states/actions 
            App.screen.fill((200,220,220))
            App.screen.blit(App.environment.surface, (App.camera.x,App.camera.y))
            
            
            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()