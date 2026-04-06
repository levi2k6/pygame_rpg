
from typing import Any, Callable, Dict
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionMenu import EnumActionMenu
from enums.enumScene import EnumScene
from game.state.game.gameState import GameState
from init.serializationRegistry import SerializationRegistry
from inputs.inputFunction import InputFunction
from serialization.serializationPlayer import SerializationPlayer
from simulation.simulationBasic import SimulationBasic


class InputMenu:

    def __init__(self, gameState: GameState, serializationPlayer: SerializationPlayer, simulationRegistry: SimulationBasic):
        self.gameState: GameState = gameState
        self.serializationPlayer: SerializationPlayer = serializationPlayer 

        self.inputs: Dict[EnumActionMenu | EnumActionBasic, InputFunction] = {
            EnumActionBasic.OK: InputFunction("Ok", self.menuSomething),
            EnumActionBasic.UP: InputFunction("Up", self.menuSomething),
            EnumActionBasic.LEFT: InputFunction("Left", self.menuSomething),
            EnumActionBasic.DOWN: InputFunction("Right", self.menuSomething),
            EnumActionBasic.RIGHT: InputFunction("Down", self.menuSomething),
            EnumActionBasic.NAVIGATE_WORLD: InputFunction("Navigate World", simulationRegistry.navigateWorld),
            EnumActionMenu.CREATE_CHARACTER: InputFunction("Create Character", self.serializationPlayer.saveTeam), 
            EnumActionMenu.TEST: InputFunction("menuSomething", self.menuSomething),
        }

    def menuSomething(self): 
        self.gameState.currentScene = EnumScene.WORLD 


    def test(self):
        print("Menu test")

