

from typing import List
from pygame import Rect, Vector2

from core.form import Form
from init.worldRegistry import WorldRegistry
from loadedAssets.assetsRegistry import AssetsRegistry
from world.tile import Tile
from world.traveler import Traveler
from world.world import World


class SimulationTileGeneration: 

    def __init__(self, worldRegistry: WorldRegistry, assetsRegistry: AssetsRegistry):
        self.world = worldRegistry.world
        self.textures = assetsRegistry.textures

    def generateTiles(self):
        rect: Rect = self.world.rect 
        width: int = self.world.width 
        height: int = self.world.height
        tiles: List[List[Tile]] = self.world.tiles
        tilesWidth: float = self.world.tilesWidth 
        tilesHeight: float = self.world.tilesHeight 
        tileOrigin: Vector2 = Vector2(0, 0)

        #generate tiles
        rowY: float = self.world.tileOrigin.y
        rowX: float = self.world.tileOrigin.x
        for _ in range(height):
            row: List[Tile] = []
            #genrate row
            for _ in range(height):
                rect: Rect = Rect(rowX, rowY, width, height)
                tile: Tile = Tile(rect, self.textures["forsen"])
                row.append(tile)
                rowX += width
            #move down for new row
            rowY += height
            #reset x position
            rowX = tileOrigin.x  
            tiles.append(row)
        pass

pass
