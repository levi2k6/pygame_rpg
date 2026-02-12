from pygame import Vector2
from Entity.entity import Entity
from Entity.monsters.goblin import Goblin
from Initialization.assets import Assets
from Properties.form import Form

class SpawnSystem:

    def __init__(self, assets: Assets):
        self.assets: Assets = assets

    def spawnGoblin(self) -> Entity:
        position: Vector2 = Vector2(600, 100)
        size: Vector2 = Vector2(200, 200)
        sprite = self.assets.data["forsen"]
        form: Form = Form(position, size, sprite)
        goblin = Goblin("goblin", form)
        return goblin


