from typing import Tuple
import pygame
from Entity.entity import Entity
from Initialization.display import Display
from Scene.scene import Scene

class RenderSystem:

    def __init__(self, display: Display):
        self.display = display

    def renderTexture(self, texture, size: Tuple[int, int], position: Tuple[int, int]):
        scaled_sprite = pygame.transform.scale(texture, size)
        sprite_x = position[0]- (position[0] / 2) 
        sprite_y = position[1] - (position[1] / 2) 
        self.display.screen.blit(scaled_sprite, (sprite_x, sprite_y))


    def renderEntity(self, entity: Entity):
        self.renderTexture(entity.sprite, (entity.spriteHeight, entity.spriteWidth), (entity.x, entity.y));
        pygame.draw.circle(self.display.screen, (255, 0, 0), (entity.x, entity.y), 10)


    def renderScene(self, scene: Scene):







