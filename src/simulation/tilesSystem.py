from typing import List

from pygame import Rect, Surface, Vector2
from Initialization.assets import Assets
from Properties.form import Form
from Scene.WorldScene.tile import Tile
from Scene.WorldScene.traveler import Traveler
from world.world import World


class TileSystem:

    def __init__(self, world: World, textures: dict):
        self.world = world
        self.textures = textures 

    def generateTiles(self): 
        rowY = self.world.tileInitPos.y
        rowX = self.world.tileInitPos.x
        for _ in range(self.world.height):
            row: List[Tile] = []
            for _ in range(self.world.width):
                rect: Rect = Rect(rowX, rowY, self.world.width, self.world.height)
                tile: Tile = Tile(rect, self.textures["forsen"])
                row.append(tile)
                rowX += self.world.width
            rowY += self.world.height
            rowX = self.world.tileInitPos.x

            self.world.tiles.append(row)
   
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

