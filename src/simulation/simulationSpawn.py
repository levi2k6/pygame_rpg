from pygame import Vector2
from world.entities.entity import Entity
from world.entities.goblin import Goblin
from loadedAssets.assetsRegistry import AssetsRegistry 
from core.form import Form

class SimulationSpawn:

    def __init__(self):
        pass

    def spawnGoblin(self) -> Entity:
        # position: Vector2 = Vector2(600, 100)
        # size: Vector2 = Vector2(200, 200)
        # sprite = self.assets.data["forsen"]
        # form: Form = Form(position, size, sprite)
        goblin = Goblin("goblin")
        return goblin


