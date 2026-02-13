from pygame import Surface, Vector2
from Entity.entity import Entity
from Entity.human import Human
from Initialization.assets import Assets
from Properties.form import Form

class GameState: 
    def __init__(self, assets: Assets):
        self.player: Human | None = None
        self.companion: Entity | None = None 
        self.assets = assets 
        self.setPlayer()

        #debugging
        self.isPositionShow: bool = False

    def setPlayer(self): 
        position: Vector2 = Vector2(100, 100)
        size: Vector2 = Vector2(100, 100)
        sprite: Surface = self.assets.data["forsen"]
        form: Form = Form(position, size, sprite)
        human: Human = Human("player", form)
        self.player = human

    def setIsPositionShow(self):
        print("isPositionShow is changed to: ", self.isPositionShow)
        self.isPositionShow = not self.isPositionShow


