# from abc import abstractmethod
import pygame
import math
from pygame import Surface, Vector2 

class Entity:
    def __init__(self, name: str, position: Vector2, size: Vector2, sprite: Surface):
        self.name: str = name
        self.position: Vector2 = position 
        self.size: Vector2 = size
        self.rotation: float = 0 
        self.sprite: Surface = sprite

        self.setSize(self.size) 

    def setSize(self, size: Vector2):
        self.size = size
        scaledSprite = pygame.transform.scale(self.sprite, self.size) 
        self.sprite = scaledSprite

    def setRotation(self, angle: float):
        angle_rad = math.pi / angle 
        angle_degree = math.degrees(angle_rad)
        self.rotation = angle_degree
        scaledSprite = pygame.transform.rotate(self.sprite, self.rotation)
        self.sprite = scaledSprite

