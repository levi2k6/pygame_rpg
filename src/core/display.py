from typing import Tuple
import pygame
from pygame import Vector2

class Display:

    def __init__(
        self, 
        size: Tuple[int, int],
        caption: str
    ) -> None:
        self.width: int = size[0]
        self.height: int = size[1]
        self.caption = caption 
        self.startDisplay()
        pass 

    def startDisplay(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)


