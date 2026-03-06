from typing import List

from Initialization.assets import Assets
from Properties.form import Form
from Scene.WorldScene.tile import Tile
from Scene.WorldScene.traveler import Traveler
from Scene.scene import Scene
from pygame  import Rect, Surface, Vector2


class tileSystem: 
    def __init__(self, assets: Assets):
        super().__init__()
        self.worldWidth = 5 
        self.worldHeight = 5 
        self.tiles: List[List[Tile]] = []
        self.tilesWidth: float = 100 
        self.tilesHeight: float = 100 
        self.initPos: Vector2 = Vector2(0, 0)
        self.assets = assets
        self.traveler: Traveler | None = None

        self.generateTiles()
        pass


    def generateTiles(self):
        rowY = self.initPos.y
        rowX = self.initPos.x 
        for _ in range(self.worldHeight):
            row: List[Tile] = []
            for _ in range(self.worldWidth):
                rect: Rect = Rect(rowX, rowY, self.tilesWidth, self.tilesHeight) 
                tile: Tile = Tile(rect, self.assets.data["forsen"])
                row.append(tile)
                rowX += self.tilesWidth
            rowY += self.tilesHeight
            rowX = self.initPos.x

            self.tiles.append(row)

    def spawnTraveler(self):
        position: Vector2 = Vector2(0, 0)
        size: Vector2 = Vector2(50, 50)
        sprite: Surface = self.assets.data["forsen"]
        form: Form = Form(position, size, sprite)
        traveler: Traveler = Traveler(form) 
        self.traveler = traveler 

        pass

    def occupyTile(self, x: int, y: int):
        if self.traveler == None: 
            raise RuntimeError("Traveler does not exists")
        targetTile = self.tiles[y][x]
        targetTile.occupy = self.traveler 
        self.traveler.tileX = x
        self.traveler.tileY = y
        newTravlerPosition = Vector2(targetTile.rect.centerx, targetTile.rect.centery)
        self.traveler.form.position = newTravlerPosition


