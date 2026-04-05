
from enums.enumScene import EnumScene
from init.gameStateRegistry import StateRegistry
from ui.uiRegistry import UIRegistry


class SimulationUi:
    def __init__(self, stateRegistry: StateRegistry, uiRegistry: UIRegistry):
        self.gameState = stateRegistry.gameState
        self.uiMenu = uiRegistry.uiMenu
        self.uiWorld = uiRegistry.uiWorld
        pass

    def uiVisibilityHandler(self): 
        if self.gameState.currentScene == EnumScene.MENU:
            for ui in self.uiMenu.uis:
                ui.show()
            for ui in self.uiWorld.uis:
                ui.hide()
        elif self.gameState.currentScene == EnumScene.WORLD:
            for ui in self.uiMenu.uis:
                ui.hide()
            for ui in self.uiWorld.uis:
                ui.show()



