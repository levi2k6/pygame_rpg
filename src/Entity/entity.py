# from abc import abstractmethod
import pygame

from util.types.entityPropertyTypes import Vec2

class Entity:
    def __init__(self, name: str, position: Vec2, collisionShape, size: Vec2, sprite):
        self.name: str = name
        self.position: Vec2 = position
        self.collisionShape = collisionShape
        self.size: Vec2 = size
        self.sprite = sprite

    def draw(self, screen):
        scaled_sprite = pygame.transform.scale(self.sprite, (self.size.x, self.size.y))
        sprite_x = self.position.x - (self.size.x / 2) 
        sprite_y = self.position.y - (self.size.y / 2) 
        screen.blit(scaled_sprite, (sprite_x, sprite_y))
        # pygame.draw.circle(screen, self.bodyColor, (self.x, self.y), 10)
    pass


