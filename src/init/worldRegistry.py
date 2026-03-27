from pygame import Rect, Vector2
from Initialization.assets import Assets
from Initialization.display import Display
from Properties.form import Form
from Scene.WorldScene.traveler import Traveler
from world.combatScene import CombatScene
from world.world import World

class WorldRegistry:

    def __init__(self, assets: Assets, display: Display):
        self.initWorld(assets)
        self.initCombatScene(display)

    def initWorld(self, assets: Assets):
        rect: Rect = Rect(0, 0, 1000, 1000) 
        width: int = 5 
        height: int = 5
        tilesWidth: float = 100
        tilesHeight: float = 100
        tileOrigin: Vector2 = Vector2(0, 0)

        form: Form = Form(Vector2(0, 0), Vector2(20, 20), assets.data["forsen"])
        traveler: Traveler = Traveler(form) 

        self.world: World = World(rect, width, height, tilesWidth, tilesHeight, tileOrigin, traveler)
        pass

    def initCombatScene(self, display: Display):
        team1x = display.size.x / 4
        team1y = display.size.y / 2
        team1Position = Vector2(team1x, team1y)

        team2x = (display.size.x / 4) * 3
        team2y = display.size.y / 2
        team2Position = Vector2(team2x, team2y)
        self.combatScene: CombatScene = CombatScene(team1Position, team2Position)

        pass

