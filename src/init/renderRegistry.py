from render import rendererBasic
from render.rendererScene import RendererScene
from render.rendererSprite import RendererSprite
from state.game.gameState import GameState
from state.settings.display import Display
from init.coreRegistry import CoreRegistry
from init.stateRegistry import StateRegistry
from init.worldRegistry import WorldRegistry
from render.camera import Camera
from render.rendererBasic import RendererBasic
from render.rendererUi import RendererUI
from render.rendererWorld import RendererWorld
from ui.uiRegistry import UIRegistry
from world.world import World


class RenderRegistry:
    def __init__(self, stateRegistry: StateRegistry, worldRegistry: WorldRegistry, uiRegistry: UIRegistry):
        self.camera = self.initCamera(stateRegistry.settingsState.display)
        self.rendererBasic = self.initRendererBasic(stateRegistry.gameState, stateRegistry.settingsState.display, self.camera)
        self.rendererWorld = self.initRendererWorld(stateRegistry, stateRegistry.settingsState.display, worldRegistry.world, self.camera)
        self.rendererUi = self.initRendererUI(uiRegistry, stateRegistry) 
        self.rendererScene = self.initRendererScene(stateRegistry, self.rendererWorld)
        self.rendererSprite = self.initRendererSprite(self.rendererBasic)
        pass

    def initCamera(self, display: Display): 
        return Camera(display) 

    def initRendererBasic(self, gameState: GameState, display: Display, camera: Camera): 
        return RendererBasic(gameState, display, camera)

    def initRendererWorld(self, stateRegistry: StateRegistry, display: Display, world: World, camera: Camera):
        return RendererWorld(stateRegistry, display, self.rendererBasic,  world, camera)

    def initRendererUI(self, uiRegistry: UIRegistry, stateRegistry: StateRegistry):
        return RendererUI(uiRegistry, stateRegistry) 

    def initRendererScene(self, stateRegistry: StateRegistry, rendererWorld: RendererWorld):
        return RendererScene(stateRegistry, rendererWorld)

    def initRendererSprite(self, rendererBasic: RendererBasic): 
        return RendererSprite(rendererBasic)
