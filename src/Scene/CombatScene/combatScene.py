from typing import List

from pygame.math import Vector2

from Entity.entity import Entity
from Entity.human import Human
from Entity.marker import Marker
from GameState.gameState import GameState
from Initialization.display import Display
from Scene.CombatScene.combatSystem import CombatSystem
from Scene.CombatScene.spawnSystem import SpawnSystem
from Scene.scene import Scene

class CombatScene(Scene):
    def __init__(self, gameState: GameState, combatSystem: CombatSystem, spawnSystem: SpawnSystem, display: Display):
        super().__init__()
        self.gameState = gameState
        self.combatSystem = combatSystem
        self.entities: dict = {}
        self.spawnSystem = spawnSystem
        self.display = display

        self.createMarkers()
        self.spawnEntities()

    def createMarkers(self):
        x = self.display.size.x / 4
        y = self.display.size.y / 2
        position: Vector2 = Vector2(x, y)
        self.markers.append(Marker("marker1", position))

        x = (self.display.size.x / 4) * 3
        y = self.display.size.y / 2
        position: Vector2 = Vector2(x, y)
        self.markers.append(Marker("marker2", position))

    def spawnEntities(self):
        #init entities
        team1: List[Entity] = [] 
        player: Human | None = self.gameState.player
        if not player: raise RuntimeError("Player is not found") 
        team1.append(player)
        companion: Entity | None = self.gameState.companion
        if companion: team1.append(companion) 
        
        team1.append(player)

        team2: List[Entity] = []
        goblin = self.spawnSystem.spawnGoblin()
        team2.append(goblin)

        self.entities["team1"] = team1
        self.entities["team2"] = team2

        #position entities
        marker1: Marker = self.getMarker("marker1")
        if marker1 is None: raise RuntimeError("Marker is not foud")
        self.entities["team1"][0].form.position = marker1.position

        marker2: Marker = self.getMarker("marker2")
        if marker2 is None: raise RuntimeError("Marker is not foud")
        self.entities["team2"][0].form.position = marker2.position

        print("team1: ", self.entities["team1"])
        print("team2: ", self.entities["team2"])
        pass


