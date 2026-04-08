
from enum import Enum
from pygame import Color, Rect, Vector2, draw

from enums.enumScene import EnumScene
from init.stateRegistry import StateRegistry
from render.rendererWorld import RendererWorld

class RendererScene:

    def __init__(self, stateRegistry: StateRegistry, rendererWorld: RendererWorld):
        self.gameState = stateRegistry.gameState
        self.rendererWorld = rendererWorld

        self.lastScene: Enum | None = None 
        pass

    def renderScene(self):
        if self.gameState.currentScene == EnumScene.WORLD:
            self.rendererWorld.renderWorld()




