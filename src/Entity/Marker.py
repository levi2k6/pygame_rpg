import pygame

class Marker:
    x: float = 0 
    y: float = 0
    color: tuple = (255, 0, 0)

    def setPosition(self, x, y): 
        self.x = x
        self.y = y
        return self


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
        



