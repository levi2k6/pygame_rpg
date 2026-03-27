
from world.entities.entity import Entity
from world.entities.human import Human


class Team:
    def __init__(self, player: Human, companion: Entity | None, filename: str):
        self.player: Human = player
        self.companion: Entity | None = companion
        self.filename: str = filename
