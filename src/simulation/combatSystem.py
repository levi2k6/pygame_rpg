from typing import List
from pygame import Vector2
from world.entities.entity import Entity
from world.entities.human import Human
from world.entities.marker import Marker
from gameState.gameState import GameState
from Initialization.display import Display
from simulation.spawnSystem import SpawnSystem 
from gameState.player import Player
from world.team import Team


class CombatSystem:

    def __init__(self, gameState: GameState, spawnSystem: SpawnSystem, display: Display, player: Player):
        super().__init__()
        self.gameState = gameState
        self.team1: dict = {"player": None, "companion": None}
        self.team2: dict = {"enemy1": None, "enemy2": None}
        self.turnQueue = []


        self.spawnSystem = spawnSystem
        self.display = display
        self.player = player


    def spawnEntities(self):
        #init entities
        playerCurrentTeam: Team | None = self.player.currentTeam
        if playerCurrentTeam == None:
            raise RuntimeError("Player entity is empty")

        self.team1["player"] = playerCurrentTeam.player
        self.team1["companion"] = playerCurrentTeam.companion

        self.team2["enemy1"] = self.spawnSystem.spawnGoblin()
        self.team2["enemy2"] = self.spawnSystem.spawnGoblin()
        pass


