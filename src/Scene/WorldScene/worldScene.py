from typing import List

from Scene.WorldScene.tileSystem import TileSystem
from Scene.scene import Scene 

class WorldScene(Scene):
    def __init__(self, tileSystem: TileSystem):
        super().__init__()
        self.tileSystem = tileSystem

        self.tileSystem.generateTiles()  
        self.tileSystem.spawnTraveler()






