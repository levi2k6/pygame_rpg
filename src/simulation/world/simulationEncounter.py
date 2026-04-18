import random

from enums.enumScene import EnumScene
from init.stateRegistry import StateRegistry
from state.game.gameState import GameState


class SimulationEncounter:

    def __init__(self, stateRegistry: StateRegistry):
        self.gameState: GameState = stateRegistry.gameState 
        pass

    def rollEncounter(self):
        if random.random() < 0.05:
            print("encounter found!")
            self.gameState.currentScene = EnumScene.COMBAT
        else:
            print("nothing found")








