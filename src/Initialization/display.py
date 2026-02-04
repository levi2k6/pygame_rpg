from typing import Tuple
import pygame

class Display:

    def __init__(
        self, 
        width: int,
        height: int,
        caption: str
    ) -> None:
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption) 
        pass 

    def setColor(self, color: Tuple[int, int, int]):
        self.screen.fill(color);

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width 

    def setHeight(self, height):
        self.height = height

    def getheight(self):
        return self.height

    

