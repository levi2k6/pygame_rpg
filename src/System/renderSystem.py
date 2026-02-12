from sys import is_finalizing
from typing import Tuple
import pygame
from pygame import Vector2, Surface
from Entity.entity import Entity
from Initialization.display import Display
from Scene.CombatScene.combatScene import CombatScene
from Scene.scene import Scene

class RenderSystem:
    def __init__(self, display: Display):
        self.display = display

    def renderTexture(self, texture: Surface, size: Vector2, position: Vector2):
        sprite_x = position.x - (size.x / 2) 
        sprite_y = position.y - (size.y / 2) 
        self.display.screen.blit(texture, (sprite_x, sprite_y))

    def renderEntity(self, entity: Entity):
        spriteRect  = entity.form.transformedSprite.get_rect(center=entity.form.position)
        self.display.screen.blit(entity.form.transformedSprite, spriteRect.topleft)

        pygame.draw.circle(self.display.screen, (255, 0, 0), entity.form.position, 10)

    def renderScene(self, scene: Scene):
        if not len(scene.backgrounds) == 0:
            for background in scene.backgrounds: 
                position: Vector2 = Vector2(self.display.size.x / 2, self.display.size.y)
                self.renderTexture(background, self.display.size, position)

        if not len(scene.props) == 0:
            for prop in scene.props: 
                self.renderTexture(prop.form.sprite, prop.form.size, prop.form.position)

        if type(scene) is CombatScene: 
            self.renderCombatScene(scene)


    def renderCombatScene(self, scene: CombatScene): 
        if len(scene.entities["team1"]) != 0:
            for entity in scene.entities["team1"]: 
                self.renderEntity(entity)

        if len(scene.entities["team2"]) != 0:
            for entity in scene.entities["team2"]: 
                self.renderEntity(entity)
