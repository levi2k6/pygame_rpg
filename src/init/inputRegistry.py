import pygame
from game.state.game.gameState import GameState
from init.gameStateRegistry import StateRegistry
from inputs.inputBasic import InputBasic
from inputs.inputMenu import InputMenu
from inputs.inputWorld import InputWorld
from serialization.serializationPlayer import SerializationPlayer


class InputRegistry:

    def __init__(self, stateRegistry: StateRegistry, serializationPlayer: SerializationPlayer):
        self.inputBasic = self.initInputBasic(stateRegistry.gameState)
        self.inputMenu = self.initInputMenu(stateRegistry.gameState, serializationPlayer) 
        self.inputWorld = self.initInputWorld(stateRegistry.gameState)
        self.serializationPlayer = serializationPlayer

    def initInputBasic(self, gameState: GameState):
        return InputBasic(gameState)

    def initInputMenu(self, gameState: GameState, serializationPlayer: SerializationPlayer):
        return InputMenu(gameState, serializationPlayer)

    def initInputWorld(self, gameState):
        return InputWorld(gameState)

            
