

from enums.enumScene import EnumScene
from core.gameState import GameState


class InputWorld:
    def __init__(self, gameState: GameState):
        self.gameState = gameState
        pass

    def test(self): 
        print("no longer saving")

    def navigateMenu(self):
        print("navigate to menu")
        self.gameState.currentScene = EnumScene.MENU



