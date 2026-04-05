from typing import Dict

from pygame_gui.core import UIElement
from game.state.gameState import GameState
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionWorld import EnumActionWorld
from enums.enumScene import EnumScene
from inputs.inputFunction import InputFunction


class InputBasic:

    def __init__(self, gameState: GameState):

        self.gameState = gameState

        self.inputs: Dict[EnumActionBasic, InputFunction] = {
            EnumActionBasic.NAVIGATE_MENU: InputFunction("Navigate Menu", self.navigateMenu), 
            EnumActionBasic.NAVIGATE_WORLD: InputFunction("Navigate World", self.navigateWorld),
            EnumActionBasic.NAVIGATE_SETTINGS: InputFunction("Navigate Settings", self.navigateSettings)
        }

        pass
        

    def navigateMenu(self):
        self.gameState.currentScene = EnumScene.MENU
        pass

    def navigateWorld(self):
        self.gameState.currentScene = EnumScene.WORLD
        pass

    def navigateSettings(self):
        self.gameState.currentScene = EnumScene.SETTINGS
        pass

    pass


