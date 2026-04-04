import pygame
from game.state.gameState import GameState
from init.gameStateRegistry import StateRegistry
from inputs.inputFunction import InputFunction 
from inputs.inputMenu import InputMenu
from inputs.inputWorld import InputWorld
from serialization import serializationPlayer
from serialization.serializationPlayer import SerializationPlayer


class InputRegistry:

    def __init__(self, stateRegistry: StateRegistry, serializationPlayer: SerializationPlayer):
        self.inputMenu = self.initInputMenu(stateRegistry.gameState, serializationPlayer) 
        self.inputWorld = self.initInputWorld(stateRegistry.gameState)
        self.serializationPlayer = serializationPlayer

    def initInputMenu(self, gameState: GameState, serializationPlayer: SerializationPlayer):
        return InputMenu(gameState, serializationPlayer)

    def initInputWorld(self, gameState):
        return InputWorld(gameState)



