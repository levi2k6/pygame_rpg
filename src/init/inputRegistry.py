import pygame
from init import simulationRegistry
from inputs.inputCombat import InputCombat
from state.game.gameState import GameState
from init.stateRegistry import StateRegistry
from init.simulationRegistry import SimulationRegistry
from inputs.inputBasic import InputBasic
from inputs.inputMenu import InputMenu
from inputs.inputWorld import InputWorld
from serialization.serializationPlayer import SerializationPlayer


class InputRegistry:

    def __init__(self, stateRegistry: StateRegistry, serializationPlayer: SerializationPlayer, simulationRegistry: SimulationRegistry):
        self.inputBasic = self.initInputBasic(stateRegistry.gameState)
        self.inputMenu = self.initInputMenu(stateRegistry.gameState, serializationPlayer, simulationRegistry) 
        self.inputWorld = self.initInputWorld(stateRegistry.gameState, simulationRegistry)
        self.inputCombat = self.initInputCombat(stateRegistry.gameState, simulationRegistry)
        self.serializationPlayer = serializationPlayer

    def initInputBasic(self, gameState: GameState):
        return InputBasic(gameState)

    def initInputMenu(self, gameState: GameState, serializationPlayer: SerializationPlayer, simulationRegistry: SimulationRegistry):
        return InputMenu(gameState, serializationPlayer, simulationRegistry)

    def initInputWorld(self, gameState, simulationRegistry: SimulationRegistry):
        return InputWorld(gameState, simulationRegistry)

    def initInputCombat(self, gameState, simulationRegistry: SimulationRegistry):
        return InputCombat(gameState, simulationRegistry)
            
