

from pygame import Color, Vector2, draw
from init.stateRegistry import StateRegistry
from state.game.gameState import GameState
from state.settings.display import Display
from world.traveler import Traveler
from render.camera import Camera
from render.rendererBasic import RendererBasic
from combat.combatScene import CombatScene
from world.world import World

class RendererWorld:

    def __init__(self, stateRegistry: StateRegistry, display: Display, rendererBasic: RendererBasic, world: World, camera: Camera):
        self.gameState = stateRegistry.gameState 
        self.debugState = stateRegistry.debugState
        self.display = display
        self.rendererBasic = rendererBasic 
        self.world = world
        self.camera = camera
        pass

    def renderWorld(self):

        if len(self.world.tiles) == 0:
            return

        self.camera.position = self.world.traveler.form.position - Vector2(self.display.screen.get_width()/2, self.display.screen.get_height()/2)

        for i in range(len(self.world.tiles)):
            for tile in self.world.tiles[i]:
                if self.debugState.isPositionShow == True:


                    color: Color = Color(255, 0, 0) 
                    topLeft = tile.rect.topleft - self.camera.position
                    topRight = tile.rect.topright - self.camera.position
                    bottomRight = tile.rect.bottomright - self.camera.position
                    bottomLeft = tile.rect.bottomleft - self.camera.position

                    draw.line(self.display.screen, color, topLeft, topRight)
                    draw.line(self.display.screen, color, topRight, bottomRight)
                    draw.line(self.display.screen, color, bottomRight, bottomLeft)
                    draw.line(self.display.screen, color, bottomLeft, topLeft)
        
        #traveler render 
        traveler: Traveler = self.world.traveler
        self.rendererBasic.renderTexture(traveler.form.transformedSprite, traveler.form.size, traveler.form.position)



    pass
