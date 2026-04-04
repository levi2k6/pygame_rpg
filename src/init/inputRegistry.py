import pygame
from game.state.gameState import GameState
from inputs.inputBasic import InputBasic
from inputs.inputCustom import InputCustom
from inputs.inputMenu import InputMenu
from inputs.inputWorld import InputWorld
from serialization.serializationPlayer import SerializationPlayer


class InputRegistry:

    def __init__(self, gameState: GameState, serializationPlayer: SerializationPlayer):
        self.inputBasic = self.initInputBasic(gameState)
        self.inputMenu = self.initInputMenu(gameState, serializationPlayer) 
        self.inputWorld = self.initInputWorld(gameState)
        self.serializationPlayer = serializationPlayer

    def initInputBasic(self, gameState: GameState):
        return InputBasic(gameState)

    def initInputMenu(self, gameState: GameState, serializationPlayer: SerializationPlayer):
        return InputMenu(gameState, serializationPlayer)

    def initInputWorld(self, gameState):
        return InputWorld(gameState)


    def initInputCustom(self, inputBasic: InputBasic, inputMenu: InputMenu, inputWorld: InputWorld):
        initCustom = InputCustom()

        if len(initCustom.customKeys) <= 0:   
            letterKeys = [
                    getattr(pygame, f"K_{chr(c)}")
                    for c in range(ord('a'), ord('z')+1)
            ]

            

