import pygame
from pygame import Surface, Vector2

class Form:
    def __init__(self, position: Vector2, size: Vector2, sprite: Surface):
        self.position: Vector2 = position 
        self.size: Vector2 = size
        self.rotation: float = 0 
        self.sprite: Surface = sprite
        self.scaledSprite: Surface = sprite
        self.transformedSprite: Surface = sprite
        self.resizeSprite(self.size)

    def resizeSprite(self, size: Vector2):
        self.scaledSprite = pygame.transform.scale(self.sprite, size)
        self.transformedSprite = self.scaledSprite 

    def rotateSprite(self, angle: float):
        rotated = pygame.transform.rotate(self.scaledSprite, angle)
        self.transformedSprite = rotated
