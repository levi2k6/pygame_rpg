

from enums.enumActionBasic import EnumActionBasic
from game.state.gameState import GameState
from enums.enumActionWorld import EnumActionWorld
from inputs.inputFunction import InputFunction


class InputWorld:
    def __init__(self, gameState: GameState):
        self.gameState = gameState
        self.inputs = {
            EnumActionBasic.NAVIGATE_MENU: InputFunction("Menu", self.test),
            EnumActionWorld.TEST: InputFunction("Test", self.worldSomething)
        }

    def test(self): 
        print("no longer saving")

    def worldSomething(self):
        print("world something")





