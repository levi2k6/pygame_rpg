
import pygame
from enums.enumScene import EnumScene
from init.serializationRegistry import SerializationRegistry
from serialization import serializationPlayer
from serialization.serializationPlayer import SerializationPlayer
from state.debug.debugState import DebugState
from state.settings.display import Display
from state.game.gameState import GameState
from state.game.player import Player
from state.settings.keymapsSettings import KeymapsSettings
from state.settings.settingsState import SettingsState


class StateRegistry:

    def __init__(self, serializationRegistry: SerializationRegistry):
        self.serializationPlayer: SerializationPlayer = serializationRegistry.serializationPlayer 
        self.gameState = self.initGameState()
        self.debugState = self.initDebug()
        self.settingsState = self.initSettings()
        pass

    def initGameState(self): 
        print("initGameState")
        player: Player = Player()
        self.serializationPlayer.loadTeams(player)

        for team in player.teams: 
            print("Player: ", "name: ", team.player.name)
        return GameState(EnumScene.MENU, player)

    def initDebug(self):
        return DebugState()

    def initSettings(self):
        display = Display((800, 800), "pygame_rpg")
        pygame.display.set_caption(display.caption)
        keymapsSettings: KeymapsSettings = KeymapsSettings() 
        return SettingsState(display, keymapsSettings)


