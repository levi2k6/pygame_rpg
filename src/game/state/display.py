from typing import Tuple
import pygame
from pygame import Vector2

class Display:

    def __init__(
        self, 
        size: Tuple[int, int],
        caption: str
    ) -> None:
        self.screen = pygame.display.set_mode(size)
        self.caption = caption 
        self.startDisplay()
        pass 

    def startDisplay(self):
        pygame.display.set_caption(self.caption)


