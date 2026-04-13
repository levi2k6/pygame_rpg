

import pygame
from pygame import Surface
from core.sprite import Sprite
from world.entities.entity import Entity


class AnimationSprite: 

    def __init__(self):
        pass

    def initSprite(self, sprite: Sprite):
        scaledSprite = pygame.transform.scale(sprite.sprite, sprite.size)
        rotatedSprite = pygame.transform.rotate(scaledSprite, 0.0)
        sprite.transformedSprite = rotatedSprite 

    def resizeSprite(self, sprite: Sprite):
        scaledSprite = pygame.transform.scale(sprite.sprite, sprite.size) 
        sprite.transformedSprite = scaledSprite 

    def rotateSprite(self, sprite: Sprite, angle: float):
        rotatedSprite = pygame.transform.rotate(sprite.transformedSprite, angle)
        sprite.transformedSprite = rotatedSprite 

