from pygame import Vector2
from core.sprite import Sprite

class Traveler:

    def __init__(self, sprite: Sprite, tileX: int, tileY: int):
        self.sprite: Sprite = sprite 
        self.tileX: int = tileX
        self.tileY: int = tileY
        self.position: Vector2 = Vector2() 
        pass

