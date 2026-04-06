

from typing import Dict
from enums.enumActionBasic import EnumActionBasic
from game.state.game.gameState import GameState
from enums.enumActionWorld import EnumActionWorld
from inputs.inputFunction import InputFunction


class InputWorld:
    def __init__(self, gameState: GameState):
        self.gameState = gameState
        self.inputs: Dict[EnumActionWorld | EnumActionBasic, InputFunction] = {
            EnumActionBasic.OK: InputFunction("Ok", self.test),
            EnumActionBasic.UP: InputFunction("Travel Up", self.test),
            EnumActionBasic.LEFT: InputFunction("Travel Up", self.test),
            EnumActionBasic.DOWN: InputFunction("Travel Up", self.test),
            EnumActionBasic.RIGHT: InputFunction("Travel Up", self.test),
            EnumActionBasic.NAVIGATE_MENU: InputFunction("Menu", self.test),
            EnumActionWorld.TEST: InputFunction("Test", self.worldSomething)
        }

    def test(self): 
        print("world test")

    def worldSomething(self):
        print("world something")





