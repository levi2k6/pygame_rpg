from typing import List

from Scene.scene import Scene
from pygame  import Rect, Vector2

class WorldScene(Scene):
    def __init__(self):
        super().__init__()
        self.tiles: List[Rect] = []
        self.tilesWidth: float = 100 
        self.tilesHeight: float = 100 
        self.initPos: Vector2 = Vector2(40, 40)
        self.createTiles()
        pass

    def createTiles(self):
        #first tile init 
        newY = self.initPos.y
        newX = self.initPos.x 
        for i in range(5):
            for b in range(5):
                rectX: Rect = Rect(newX, newY, self.tilesWidth, self.tilesHeight)
                self.tiles.append(rectX)
                newX += self.tilesWidth;

            newY += self.tilesHeight 
            newX = self.initPos.x

        pass

