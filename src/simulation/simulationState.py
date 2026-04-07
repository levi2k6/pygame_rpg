from enums.enumScene import EnumScene
from state.game.gameState import GameState
from init.stateRegistry import StateRegistry
from simulation.simulationUi import SimulationUi
from world.traveler import Traveler
from render.camera import Camera
from world.entities.human import Human
from state.game.player import Player
from core.team import Team

class SimulationState:
    def __init__(self, stateRegistry: StateRegistry, simulationUi: SimulationUi):
        self.gameState = stateRegistry.gameState
        self.simulationUi = simulationUi

    def navigateWorld(self):
        self.gameState.currentScene = EnumScene.WORLD 
        self.simulationUi.uiVisibilityHandler()


