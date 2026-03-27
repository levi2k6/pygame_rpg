import pygame
from pygame import Color, Rect, Surface, Vector2, draw
from gameState.gameState import GameState
from Initialization.display import Display
from render.camera import Camera

class RendererBasic():
    def __init__(self, gameState: GameState,display: Display, camera: Camera):
        self.display = display
        self.gameState = gameState
        self.camera = camera

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

    def renderPosition(self, position: Vector2):
        # print("renderPosition")
        newPosition = position - self.camera.position
        pygame.draw.circle(self.display.screen, Color(255, 0, 0), newPosition, 5)

    def renderRect(self, rect: Rect): 
        color: Color = Color(255, 255, 0)
        topLeft = rect.topleft - self.camera.position 
        topRight = rect.topright - self.camera.position
        bottomRight = rect.bottomright - self.camera.position
        bottomLeft = rect.bottomleft - self.camera.position

        draw.line(self.display.screen, color, topLeft, topRight)
        draw.line(self.display.screen, color, topRight, bottomRight)
        draw.line(self.display.screen, color, bottomRight, bottomLeft)
        draw.line(self.display.screen, color, bottomLeft, topLeft)




