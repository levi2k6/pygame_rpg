from enums.enumScene import EnumScene
from state.settings.display import Display
from state.game.player import Player

class GameState: 
    def __init__(self, currentScene: EnumScene, player: Player):
        self.currentScene: EnumScene = currentScene
        self.player: Player = player


