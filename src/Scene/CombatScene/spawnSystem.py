from pygame import Vector2
from Entity.entity import Entity
from Entity.goblin import Goblin
from Entity.monster import Monster
from Initialization.assets import Assets

class SpawnSystem:

    def __init__(self, assets: Assets):
        self.assets: Assets = assets

    def spawnGoblin(self) -> Entity:
        position: Vector2 = Vector2(100, 100)
        size: Vector2 = Vector2(400, 400)
        sprite = self.assets.data["forsen"]
        goblin = Goblin("goblin", position, size, sprite)
        return goblin


