from enums.enumScene import EnumScene
from state.settings.display import Display
from state.game.player import Player

class GameState: 
    def __init__(self, currentScene: EnumScene, player: Player):
        self.isRunning: bool = True
        self.currentScene: EnumScene = currentScene
        self.lastScene: EnumScene | None = None
        self.player: Player = player


