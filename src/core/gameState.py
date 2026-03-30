from pygame import Surface, Vector2
from enums.enumScene import EnumScene
from world.entities.entity import Entity
from world.entities.human import Human
from Initialization.assets import Assets
from Properties.form import Form

class GameState: 
    def __init__(self, currentScene: EnumScene):
        self.currentScene: EnumScene = currentScene

        #debugging
        self.isPositionShow: bool = True 


