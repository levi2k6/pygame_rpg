from sys import is_finalizing
from typing import Tuple
import pygame
from pygame import Vector2, Surface, Color, Rect, draw 
from Entity.entity import Entity
from Entity.marker import Marker
from core.gameState import GameState
from Initialization.display import Display
from Scene.CombatScene.combatScene import CombatScene
from Scene.WorldScene.tile import Tile
from Scene.WorldScene.tileSystem import TileSystem
from Scene.WorldScene.worldScene import WorldScene
from Scene.scene import Scene
from System.camera import Camera

class RenderSystem:
    def __init__(self, display: Display, gameState: GameState, camera: Camera, tileSystem: TileSystem):
        self.display = display
        self.gameState = gameState
        self.camera = camera
        self.tileSystem = tileSystem 

    def renderCamera(self):
        self.renderPosition(Vector2(self.camera.rect.topleft))
        self.renderPosition(Vector2(self.camera.rect.topright))
        self.renderPosition(Vector2(self.camera.rect.bottomright))
        self.renderPosition(Vector2(self.camera.rect.bottomleft))
        self.renderPosition(Vector2(self.camera.rect.center))


    def renderTexture(self, texture: Surface, size: Vector2, position: Vector2):
        sprite_x = (position.x - (size.x / 2)) - self.camera.position.x 
        sprite_y = (position.y - (size.y / 2)) - self.camera.position.y
        self.display.screen.blit(texture, (sprite_x, sprite_y))

    def renderEntity(self, entity: Entity):
        newEntityPosX = entity.form.position.x - self.camera.position.x
        newEntityPosY = entity.form.position.y - self.camera.position.y
        spriteRect  = entity.form.transformedSprite.get_rect(center=(newEntityPosX, newEntityPosY))
        self.display.screen.blit(entity.form.transformedSprite, spriteRect.topleft)

        if self.gameState.isPositionShow == True:
            self.renderPosition(entity.form.position)

    def renderMarker(self, marker: Marker):
        if self.gameState.isPositionShow == True:
            self.renderPosition(marker.position)

    def renderTile(self, tile: Tile):
        if self.gameState.isPositionShow == True:
            tileRect = tile.rect
            center: Vector2 = Vector2(tileRect.centerx, tileRect.centery)
            self.renderPosition(center)
            # topLeft: Vector2 = Vector2(tile.left, tile.top)
            # self.renderPosition(topLeft)
            # topRight: Vector2 = Vector2(tile.right, tile.top)
            # self.renderPosition(topRight)
            # bottomLeft: Vector2 = Vector2(tile.left, tile.bottom)
            # self.renderPosition(bottomLeft)
            # bottomRight: Vector2 = Vector2(tile.right, tile.bottom)
            # self.renderPosition(bottomRight)
            color: Color = Color(255, 255, 0)
            topLeft = tileRect.topleft - self.camera.position 
            topRight = tileRect.topright - self.camera.position
            bottomRight = tileRect.bottomright - self.camera.position
            bottomLeft = tileRect.bottomleft - self.camera.position

            draw.line(self.display.screen, color, topLeft, topRight)
            draw.line(self.display.screen, color, topRight, bottomRight)
            draw.line(self.display.screen, color, bottomRight, bottomLeft)
            draw.line(self.display.screen, color, bottomLeft, topLeft)


    def renderPosition(self, position: Vector2):
        # print("renderPosition")
        newPosition = position - self.camera.position
        pygame.draw.circle(self.display.screen, Color(255, 0, 0), newPosition, 5)

    def renderScene(self, scene: Scene):
        # print("scene: ", type(scene.props))
        if not len(scene.backgrounds) == 0:
            for background in scene.backgrounds: 
                position: Vector2 = Vector2(self.display.size.x / 2, self.display.size.y)
                self.renderTexture(background, self.display.size, position)

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
        tileSystem: TileSystem = scene.tileSystem 

        if len(tileSystem.tiles) == 0:
            return
            # print("sceneTiles: ", scene.tiles)

        for i in range(len(tileSystem.tiles)):
            for tile in tileSystem.tiles[i]:
                self.renderTile(tile)

        if tileSystem.traveler != None:
            traveler = tileSystem.traveler
            self.renderTexture(traveler.form.transformedSprite, traveler.form.size, traveler.form.position)

        self.renderCamera()

        pass

