
from enums.enumScene import EnumScene
from game.state.debugState import DebugState
from game.state.gameState import GameState
from game.state.player import Player
from game.state.settingsState import SettingsState


class StateRegistry:

    def __init__(self):
        self.gameState = self.initGameState()
        self.debugState = self.initDebug()
        self.settings = self.initSettings()
        pass


    def initGameState(self): 
        return GameState(EnumScene.MENU)

    def initDebug(self):
        return DebugState()

    def initSettings(self):
        return SettingsState()


