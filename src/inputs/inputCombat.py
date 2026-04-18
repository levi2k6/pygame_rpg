from typing import Dict
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionCombat import EnumActionCombat
from init.simulationRegistry import SimulationRegistry
from simulation.simulationMovement import SimulationMovement
from simulation.simulationNavigation import SimulationNavigation
from state.game.gameState import GameState
from enums.enumActionWorld import EnumActionWorld
from inputs.inputFunction import InputFunction


class InputCombat:
    def __init__(self, gameState: GameState, simulationRegistry: SimulationRegistry):
        self.gameState = gameState
        self.simulationCombat = simulationRegistry.simulationCombat

        self.inputs: Dict[EnumActionCombat | EnumActionBasic, InputFunction] = {
            EnumActionBasic.OK: InputFunction("Spawn Entities", self.simulationCombat.spawnEntities),
        }


