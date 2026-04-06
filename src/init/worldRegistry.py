from typing import Dict, List
from pygame import Rect, Vector2
from core.form import Form
from game.state.settings.display import Display
from init.gameStateRegistry import StateRegistry
from world.tile import Tile
from world.traveler import Traveler
from loadedAssets.assetsRegistry import AssetsRegistry
from combat.combatScene import CombatScene
from world.world import World

class WorldRegistry:

    def __init__(self, stateRegistry: StateRegistry, assetsRegistry: AssetsRegistry):
        self.initWorld(assetsRegistry.textures)
        self.initCombatScene(stateRegistry.settingsState.display)


    def initWorld(self, textures: Dict):
        rect: Rect = Rect(0, 0, 1000, 1000) 
        width: int = 5 
        height: int = 5
        tiles: List[List[Tile]] = []
        tilesWidth: float = 100
        tilesHeight: float = 100
        tileOrigin: Vector2 = Vector2(0, 0)


        #generate tiles
        rowY: float = tileOrigin.y
        rowX: float = tileOrigin.x
        for _ in range(height):
            row: List[Tile] = []
            #genrate row
            for _ in range(height):
                rect: Rect = Rect(rowX, rowY, width, height)
                tile: Tile = Tile(rect, textures["forsen"])
                row.append(tile)
                rowX += width
            #move down for new row
            rowY += height
            #reset x position
            rowX = tileOrigin.x  
            tiles.append(row)

        form: Form = Form(Vector2(0, 0), Vector2(20, 20), textures["forsen"])
        traveler: Traveler = Traveler(form) 

        self.world: World = World(rect, width, height, tiles, tilesWidth, tilesHeight, tileOrigin, traveler)
        pass

    def initCombatScene(self, display: Display):
        team1x = display.screen.get_width() / 4
        team1y = display.screen.get_height() / 2
        team1Position = Vector2(team1x, team1y)

        team2x = (display.screen.width / 4) * 3
        team2y = display.screen.height / 2
        team2Position = Vector2(team2x, team2y)
        self.combatScene: CombatScene = CombatScene(team1Position, team2Position)

        pass

