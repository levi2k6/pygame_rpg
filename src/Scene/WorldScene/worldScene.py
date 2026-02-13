from typing import List

from Scene.scene import Scene
from pygame  import Rect

class WorldScene(Scene):
    def __init__(self):
        super().__init__()
        self.tiles: List[Rect] = []
        self.createTiles()
        pass

    def createTiles(self):
        rect: Rect = Rect(40, 40, 64, 64)
        self.tiles.append(rect)
        pass

