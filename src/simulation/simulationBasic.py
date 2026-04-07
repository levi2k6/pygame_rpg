
from enums.enumScene import EnumScene
from state.game.gameState import GameState
from init.stateRegistry import StateRegistry
from world.traveler import Traveler
from render.camera import Camera
from world.entities.human import Human
from state.game.player import Player
from core.team import Team


class SimulationBasic:
    def __init__(self, stateRegistry: StateRegistry):
        self.gameState = stateRegistry.gameState

    def navigateWorld(self):
        self.gameState.currentScene = EnumScene.WORLD 


