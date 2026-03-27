from pygame import Vector2

from gameState.gameState import GameState
from Initialization.display import Display
from Scene.CombatScene.combatSystem import CombatSystem
from Scene.CombatScene.spawnSystem import SpawnSystem


class CombatScene: 
    def __init__(self, team1Position: Vector2, team2Position: Vector2):
        super().__init__()

        self.team1: dict = {"player": None, "companion": None}
        self.team2: dict = {"enemy1": None, "enemy2": None}
        self.turnQueue = []

        self.team1Position: Vector2 = team1Position 
        self.team2Position: Vector2 = team2Position 

        # self.team1Posiiton = Vector2(self.display.size.x / 2, self.display.size.y / 2)
        # self.team2Position = Vector2( (self.display.size.x / 4) * 3, self.display.size.y / 2)


