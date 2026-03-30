import pygame
from gameState import gameState
from core.gameState import GameState
from inputs.inputFunction import InputFunction 
from inputs.inputMenu import InputMenu
from inputs.inputWorld import InputWorld
from serialization import serializationPlayer
from serialization.serializationPlayer import SerializationPlayer


class InputRegistry:

    def __init__(self, gameState: GameState, serializationPlayer: SerializationPlayer):
        self.inputMenu = self.initInputMenu(gameState, serializationPlayer) 
        self.inputWorld = self.initInputWorld(gameState)
        self.serializationPlayer = serializationPlayer

        self.menuInputs = {
                pygame.K_q: InputFunction("Play", self.inputMenu.navigateWorld),
                pygame.K_e: InputFunction("Create Character", self.serializationPlayer.saveTeam),
        }

        self.worldInputs = {
                pygame.K_q: InputFunction("Menu", self.inputWorld.navigateMenu),
                pygame.K_e: InputFunction("Test", self.inputWorld.test)
        }

    def initInputMenu(self, gameState: GameState, serializationPlayer: SerializationPlayer):
        return InputMenu(gameState, serializationPlayer)

    def initInputWorld(self, gameState):
        return InputWorld(gameState)

