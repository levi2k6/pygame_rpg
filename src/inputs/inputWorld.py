

from typing import Dict
from enums.enumActionBasic import EnumActionBasic
from init.simulationRegistry import SimulationRegistry
from simulation.simulationMovement import SimulationMovement
from simulation.simulationNavigation import SimulationNavigation
from state.game.gameState import GameState
from enums.enumActionWorld import EnumActionWorld
from inputs.inputFunction import InputFunction


class InputWorld:
    def __init__(self, gameState: GameState, simulationRegistry: SimulationRegistry):
        self.gameState = gameState
        self.simulationNavigation: SimulationNavigation = simulationRegistry.simulationNavigation
        self.simulationMovement: SimulationMovement = simulationRegistry.simulationMovement

        self.inputs: Dict[EnumActionWorld | EnumActionBasic, InputFunction] = {
            EnumActionBasic.OK: InputFunction("Ok", self.test),
            EnumActionBasic.UP: InputFunction("Travel Up", self.simulationMovement.travelUp),
            EnumActionBasic.LEFT: InputFunction("Travel Left", self.simulationMovement.travelLeft),
            EnumActionBasic.DOWN: InputFunction("Travel Down", self.simulationMovement.travelDown),
            EnumActionBasic.RIGHT: InputFunction("Travel Right", self.simulationMovement.travelRight),
            EnumActionBasic.NAVIGATE_MENU: InputFunction("Navigate Menu", self.simulationNavigation.navigateMenu),
            EnumActionWorld.TEST: InputFunction("Test", self.worldSomething)
        }

    def test(self): 
        print("world test")

    def worldSomething(self):
        print("world something")





