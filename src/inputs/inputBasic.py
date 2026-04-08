from typing import Dict

from pygame_gui.core import UIElement
from state.game.gameState import GameState
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionWorld import EnumActionWorld
from enums.enumScene import EnumScene
from inputs.inputFunction import InputFunction


class InputBasic:

    def __init__(self, gameState: GameState):

        self.gameState = gameState

        self.inputs: Dict[EnumActionBasic, InputFunction] = {
        }

        pass
        

