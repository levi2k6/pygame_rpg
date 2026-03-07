from Scene.WorldScene.tileSystem import TileSystem
from Scene.WorldScene.traveler import Traveler
from Scene.WorldScene.worldScene import WorldScene
from System.camera import Camera

class PlayerInput:
    def __init__(self, tileSystem: TileSystem):
        self.tileSystem = tileSystem


    def moveLeft(self):
        traveler = self.tileSystem.traveler
        if traveler == None: 
            raise RuntimeError("traveler not found")

        self.tileSystem.occupyTile(traveler.tileX - 1, traveler.tileY)
        pass

    def moveRight(self):
        traveler = self.tileSystem.traveler
        if traveler == None: 
            raise RuntimeError("traveler not found")

        self.tileSystem.occupyTile(traveler.tileX + 1, traveler.tileY)
        pass

    def moveUp(self):
        traveler = self.tileSystem.traveler
        if traveler == None:
            raise RuntimeError("traveler not found")

        self.tileSystem.occupyTile(traveler.tileX, traveler.tileY - 1)

    def moveDown(self):
        traveler = self.tileSystem.traveler
        if traveler == None:
            raise RuntimeError("traveler not found")

        self.tileSystem.occupyTile(traveler.tileX, traveler.tileY + 1)



