from typing import Dict, List
from pygame import Rect, Vector2
from core.sprite import Sprite
from state.settings.display import Display
from init.stateRegistry import StateRegistry
from world.tile import Tile
from world.traveler import Traveler
from loadedAssets.assetsRegistry import AssetsRegistry
from combat.combatScene import CombatScene
from world.world import World

class WorldRegistry:

    def __init__(self, stateRegistry: StateRegistry, assetsRegistry: AssetsRegistry):
        self.initWorld(assetsRegistry.textures)
        self.initCombatScene(stateRegistry.settingsState.display)


    def initWorld(self, textures: Dict):
        rect: Rect = Rect(0, 0, 1000, 1000) 
        width: int = 5
        height: int = 5 
        tiles: List[List[Tile]] = []
        tilesWidth: float = 100 
        tilesHeight: float = 100 
        tileOrigin: Vector2 = Vector2(0, 0)

        sprite: Sprite = Sprite(Vector2(0, 0), Vector2(100, 100), textures["forsen"])
        tileX = 0
        tileY = 0
        traveler: Traveler = Traveler(sprite, tileX, tileY) 

        self.world: World = World(rect, width, height, tiles, tilesWidth, tilesHeight, tileOrigin, traveler)
        pass

    def initCombatScene(self, display: Display):
        team1x = display.screen.get_width() / 4
        team1y = display.screen.get_height() / 2
        team1Position = Vector2(team1x, team1y)

        team2x = (display.screen.width / 4) * 3
        team2y = display.screen.height / 2
        team2Position = Vector2(team2x, team2y)
        self.combatScene: CombatScene = CombatScene(team1Position, team2Position)

        pass

