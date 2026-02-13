from sys import is_finalizing
from typing import Tuple
import pygame
from pygame import Vector2, Surface, Color, Rect
from Entity.entity import Entity
from Entity.marker import Marker
from GameState.gameState import GameState
from Initialization.display import Display
from Scene.CombatScene.combatScene import CombatScene
from Scene.WorldScene.worldScene import WorldScene
from Scene.scene import Scene

class RenderSystem:
    def __init__(self, display: Display, gameState: GameState):
        self.display = display
        self.gameState = gameState

    def renderTexture(self, texture: Surface, size: Vector2, position: Vector2):
        sprite_x = position.x - (size.x / 2) 
        sprite_y = position.y - (size.y / 2) 
        self.display.screen.blit(texture, (sprite_x, sprite_y))

    def renderEntity(self, entity: Entity):
        spriteRect  = entity.form.transformedSprite.get_rect(center=entity.form.position)
        self.display.screen.blit(entity.form.transformedSprite, spriteRect.topleft)

        if self.gameState.isPositionShow == True:
            self.renderPosition(entity.form.position)

    def renderMarker(self, marker: Marker):
        if self.gameState.isPositionShow == True:
            self.renderPosition(marker.position)

    def renderTile(self, tile: Rect):
        if self.gameState.isPositionShow == True:
            position: Vector2 = Vector2(tile.x, tile.y)
            self.renderPosition(position)
            position2: Vector2 = Vector2(tile.x + tile.width, tile.y + tile.height)
            self.renderPosition(position2)

    def renderPosition(self, position: Vector2):
        print("renderPosition")
        pygame.draw.circle(self.display.screen, Color(255, 0, 0), position, 5)


    def renderScene(self, scene: Scene):
        # print("scene: ", type(scene.props))
        if not len(scene.backgrounds) == 0:
            for background in scene.backgrounds: 
                position: Vector2 = Vector2(self.display.size.x / 2, self.display.size.y)
                self.renderTexture(background, self.display.size, position)

        print("prop length: ", len(scene.props))
        if not len(scene.props) == 0:
            for prop in scene.props:
                print("name: ", prop.name)
                self.renderTexture(prop.form.sprite, prop.form.size, prop.form.position)

        if not len(scene.markers) == 0:
            for marker in scene.markers:
                self.renderMarker(marker)

        if type(scene) is CombatScene: 
            self.renderCombatScene(scene)
        elif type(scene) is WorldScene:
            self.renderWorldScene(scene)

    def renderCombatScene(self, scene: CombatScene): 
        if len(scene.entities["team1"]) != 0:
            for entity in scene.entities["team1"]: 
                self.renderEntity(entity)

        if len(scene.entities["team2"]) != 0:
            for entity in scene.entities["team2"]: 
                self.renderEntity(entity)

    def renderWorldScene(self, scene: WorldScene):
        if len(scene.tiles) != 0:
            for tile in scene.tiles:
               self.renderTile(tile)
                for b in range(scene.tiles):
                    scene.tiles[b+1].x = tile.width

        pass

