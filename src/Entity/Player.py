import pygame
from Initialization import Display 
from Initialization import Assets

from .Human import Human 

class Player(Human):
    
    def __init__(self, name):
        self.name = name
        self.x = Display.width / 3
        self.y = Display.height / 3
        self.bodyColor = (255, 0, 0)
        self.body = None
        self.spriteWidth = 100 
        self.spriteHeight = 100
        self.sprite = Assets.data["forsen"]

    def setSprite(self, sprite):
        self.sprite = sprite
        return self

    def setPosition(self, x, y):
        self.x = x
        self.y = y  
        return self
    
    def draw(self, screen):
        scaled_sprite = pygame.transform.scale(self.sprite, (self.spriteWidth, self.spriteHeight))
        sprite_x = self.x - (self.spriteWidth / 2) 
        sprite_y = self.y - (self.spriteHeight / 2) 
        screen.blit(scaled_sprite, (sprite_x, sprite_y))
        pygame.draw.circle(screen, self.bodyColor, (self.x, self.y), 10)





