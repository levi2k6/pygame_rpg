from typing import List

from pygame import Rect, Surface, Vector2
from loadedAssets.assetsRegistry import AssetsRegistry 
from core.form import Form
from world.tile import Tile
from world.traveler import Traveler
from world.world import World


class SimulationMovement:

    def __init__(self, world: World, textures: dict):
        self.world = world
        self.textures = textures 

    def spawnTravelerInTiles(self): 
        traveler = self.world.traveler
        self.occupyTile(traveler.tileX, traveler.tileY)

    def occupyTile(self, x: int, y: int):
        traveler = self.world.traveler

        if x < 0 or x > self.world.width-1:
            print("boundary x exceeded")
            return
        if y < 0 or y > self.world.height-1:
            print("boundary y exceeded")
            return
        
        print("x: ", x)
        print("y: ", y)
        print(-self.world.height+1)

        targetTile = self.world.tiles[y][x]
        targetTile.occupy = traveler 
        traveler.tileX = x
        traveler.tileY = y
        newTravlerPosition = Vector2(targetTile.rect.centerx, targetTile.rect.centery)
        traveler.form.position = newTravlerPosition

