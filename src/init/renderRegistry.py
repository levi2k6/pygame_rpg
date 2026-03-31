from pygame import CONTROLLER_AXIS_TRIGGERRIGHT
from core.gameState import GameState
from Initialization.display import Display
from init.coreRegistry import CoreRegistry
from render.camera import Camera
from render.rendererBasic import RendererBasic
from render.rendererUi import RendererUI
from render.rendererWorld import RendererWorld
from world.world import World


class RenderRegistry:
    def __init__(self, coreRegistry: CoreRegistry, world: World):
        self.camera = self.initCamera(coreRegistry.display)
        self.rendererBasic = self.initRendererBasic(coreRegistry.gameState, coreRegistry.display, self.camera)
        self.rendererWorld = self.initRendererWorld(coreRegistry.gameState, coreRegistry.display, world, self.camera)
        self.rendererUi = self.initRendererUI() 
        pass

    def initCamera(self, display: Display): 
        return Camera(display) 

    def initRendererBasic(self, gameState: GameState, display: Display, camera: Camera): 
        return RendererBasic(gameState, display, camera)

    def initRendererWorld(self, gameState: GameState, display: Display, world: World, camera: Camera):
        return RendererWorld(gameState, display, self.rendererBasic,  world, camera)

    def initRendererUI(self):
        return RendererUI() 
