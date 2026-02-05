import pygame
from Entity.entity import Entity
from Initialization.display import Display

class RenderSystem:
    def __init__(self, display: Display):
        self.display = display

    def draw(self. entity: Entity):
        scaled_sprite = pygame.transform.scale(self.sprite, (self.spriteWidth, self.spriteHeight))
        sprite_x = self.x - (self.spriteWidth / 2) 
        sprite_y = self.y - (self.spriteHeight / 2) 
        self.display.screen.blit(scaled_sprite, (sprite_x, sprite_y))
        pygame.draw.circle(screen, self.bodyColor, (self.x, self.y), 10)







