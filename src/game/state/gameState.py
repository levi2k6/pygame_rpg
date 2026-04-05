from enums.enumScene import EnumScene
from game.state.display import Display
from game.state.player import Player

class GameState: 
    def __init__(self, currentScene: EnumScene, player: Player):
        self.currentScene: EnumScene = currentScene
        self.player: Player = player


