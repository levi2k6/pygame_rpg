from typing import List
from pygame import Rect, Vector2

from world.tile import Tile
from world.traveler import Traveler
from combat.combatScene import CombatScene

class World:
    def __init__(
            self,
            rect: Rect,
            width: int,
            height: int,
            tiles: List[List[Tile]], 
            tilesWidth: float,
            tilesHeight: float,
            tileOrigin: Vector2,
            traveler: Traveler,
    ):
        self.rect: Rect = rect
        self.width: int = width 
        self.height: int = height 
        self.tiles: List[List[Tile]] = tiles 
        self.tilesWidth: float = tilesWidth
        self.tilesHeight: float = tilesHeight 
        self.tileInitPos: Vector2 = tileOrigin 
        self.traveler: Traveler = traveler


