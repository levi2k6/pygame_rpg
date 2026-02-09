from Entity.entity import Entity
from Entity.human import Human

class GameState: 
    def __init__(self):
        self.player: Human | None = None
        self.companion: Entity | None = None 

