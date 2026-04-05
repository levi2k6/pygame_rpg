
import pygame
from enums.enumScene import EnumScene
from game.state.debugState import DebugState
from game.state.display import Display
from game.state.gameState import GameState
from game.state.player import Player
from game.state.settingsState import SettingsState


class StateRegistry:

    def __init__(self):
        self.gameState = self.initGameState()
        self.debugState = self.initDebug()
        self.settingsState = self.initSettings()
        pass

    def initGameState(self): 
        player: Player = Player()
        return GameState(EnumScene.MENU, player)

    def initDebug(self):
        return DebugState()

    def initSettings(self):
        display = Display((800, 800), "pygame_rpg")
        pygame.display.set_caption(display.caption)
        return SettingsState(display)


