
import pygame
from enums.enumScene import EnumScene
from state.debug.debugState import DebugState
from state.settings.display import Display
from state.game.gameState import GameState
from state.game.player import Player
from state.settings.keymapsSettings import KeymapsSettings
from state.settings.settingsState import SettingsState


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
        keymapsSettings: KeymapsSettings = KeymapsSettings() 
        return SettingsState(display, keymapsSettings)


