from typing import List
from pygame import Vector2
from world.entities.entity import Entity
from world.entities.human import Human
from world.entities.marker import Marker
from game.state.gameState import GameState
from core.display import Display
from simulation.simulationSpawn import SpawnSystem 
from game.state.player import Player
from game.state.team import Team


class SimulationCombat:

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


