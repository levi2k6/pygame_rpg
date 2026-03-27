from gameState.gameState import GameState
from Initialization.display import Display
from render.camera import Camera
from render.rendererBasic import RendererBasic
from render.rendererWorld import RendererWorld
from world.world import World


class RenderRegistry:
    def __init__(self, gameState: GameState, display: Display, world: World, camera: Camera):
        self.rendererBasic = self.initRendererBasic(gameState, display, camera)
        self.rendererWorld = self.initRendererWorld(gameState, display, world, camera)
        pass

    def initRendererBasic(self, gameState: GameState, display: Display, camera: Camera): 
        return RendererBasic(gameState, display, camera)

    def initRendererWorld(self, gameState: GameState, display: Display, world: World, camera: Camera):
        return RendererWorld(gameState, display, self.rendererBasic,  world, camera)

