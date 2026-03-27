from typing import List
from pygame import Rect, Vector2

from Scene.WorldScene.tile import Tile
from Scene.WorldScene.traveler import Traveler
from world.combatScene import CombatScene

class World:
    def __init__(
            self,
            rect: Rect,
            width: int,
            height: int,
            tilesWidth: float,
            tilesHeight: float,
            tilesInitPos: Vector2,
            traveler: Traveler,
    ):
        self.rect: Rect = rect
        self.width: int = width 
        self.height: int = height 
        self.tiles: List[List[Tile]] = [] 
        self.tilesWidth: float = tilesWidth
        self.tilesHeight: float = tilesHeight 
        self.tileInitPos: Vector2 = tilesInitPos 
        self.traveler: Traveler = traveler


