# from abc import abstractmethod
import pygame

class Entity:
    def __init__(self, name, x, y, collisionShape, spriteWidth, spriteHeight, sprite):
        self.name = name
        self.x = x 
        self.y = y
        self.collisionShape = collisionShape
        self.spriteWidth = spriteWidth 
        self.spriteHeight = spriteHeight 
        self.sprite = sprite

    def draw(self, screen):
        scaled_sprite = pygame.transform.scale(self.sprite, (self.spriteWidth, self.spriteHeight))
        sprite_x = self.x - (self.spriteWidth / 2) 
        sprite_y = self.y - (self.spriteHeight / 2) 
        screen.blit(scaled_sprite, (sprite_x, sprite_y))
        # pygame.draw.circle(screen, self.bodyColor, (self.x, self.y), 10)

    pass


