from enums.enumScene import EnumScene
from game.state.game.gameState import GameState
from init.gameStateRegistry import StateRegistry
from simulation.simulationUi import SimulationUi
from world.traveler import Traveler
from render.camera import Camera
from world.entities.human import Human
from game.state.game.player import Player
from game.state.game.team import Team

class SimulationState:
    def __init__(self, stateRegistry: StateRegistry, simulationUi: SimulationUi):
        self.gameState = stateRegistry.gameState
        self.simulationUi = simulationUi

    def navigateWorld(self):
        self.gameState.currentScene = EnumScene.WORLD 
        self.simulationUi.uiVisibilityHandler()


