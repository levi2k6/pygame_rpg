from typing import List
from Entity.entity import Entity
from Entity.human import Human
from GameState.gameState import GameState
from Scene.CombatScene.combatSystem import CombatSystem
from Scene.CombatScene.spawnSystem import SpawnSystem
from Scene.scene import Scene
from System import UISystem 

class CombatScene(Scene):

    def __init__(self, gameState: GameState, combatSystem: CombatSystem, spawnSystem: SpawnSystem):
        self.gameState = gameState
        self.combatSystem = combatSystem
        self.entities: dict = {}
        
    def spawnEntities(self):
        team1: List[Entity] = [] 
        player: Human = self.gameState.player
        if not player: 
            raise RuntimeError("Player is not found") 
        team1.append(player)
        companion: Entity = self.gameState.companion
        if companion: team1.append(companion) 
        
        team1.append(self.gameState.player)

        team2: List[Entity] = []
        goblin = self.spawnSystem.spawnGoblin()
        team2.append(goblin)

        self.entities["team1"] = team1
        self.entities["team2"] = team2
        pass




