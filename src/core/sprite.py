import pygame
from pygame import Surface, Vector2

class Sprite:
    def __init__(self, position: Vector2, size: Vector2, sprite: Surface):
        self.position: Vector2 = position 
        self.size: Vector2 = size
        self.rotation: float = 0 
        self.sprite: Surface = sprite
        self.transformedSprite: Surface = sprite


