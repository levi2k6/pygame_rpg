import pygame
from pygame import Vector2

class Display:

    def __init__(
        self, 
        size: Vector2,
        caption: str
    ) -> None:
        self.size = size
        self.caption = caption 
        pass 

    def startDisplay(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption


