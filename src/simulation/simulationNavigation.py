
from enums.enumScene import EnumScene
from init.stateRegistry import StateRegistry
from state.game.gameState import GameState

class SimulationNavigation:

    def __init__(self, gameState: GameState):
        self.gameState = gameState
        pass

    def navigateMenu(self):
        self.gameState.currentScene = EnumScene.MENU 

    def navigateWorld(self):
        self.gameState.currentScene = EnumScene.WORLD

