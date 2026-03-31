from pygame import Rect, Vector2, display
from pygame_gui import UIManager
from Initialization.display import Display
from core.eventHandler import EventHandler
from core.player import Player
from enums.enumScene import EnumScene
from core.gameState import GameState


class CoreRegistry:
    def __init__(self):
        self.display = self.initDisplay() 
        self.gameState = self.initGameState() 
        self.player = self.initPlayer()
        self.uiManager = self.initUiManager()

    def initDisplay(self):
        return Display((800, 800), "pygame_rpg")

    def initGameState(self): 
        return GameState(EnumScene.MENU)

    def initPlayer(self): 
        return Player()

    def initUiManager(self): 
        displaySize = (self.display.width, self.display.height)
        return UIManager(displaySize)

