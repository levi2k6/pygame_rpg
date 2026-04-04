from pygame import Rect, Vector2, display
from core.display import Display
from game.state.player import Player
from enums.enumScene import EnumScene

class CoreRegistry:
    def __init__(self):
        self.display = self.initDisplay() 
        self.player = self.initPlayer()

    def initDisplay(self):
        return Display((800, 800), "pygame_rpg")

    def initPlayer(self): 
        return Player()

