from pygame import Rect, Surface 

from Scene.WorldScene.traveler import Traveler

class Tile:
    def __init__(self, rect: Rect, sprite: Surface):
        self.rect: Rect = rect
        self.occupy: Traveler | None = None
        self.sprite: Surface = sprite
