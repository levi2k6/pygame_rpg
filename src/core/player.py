from typing import List
from world.entities.entity import Entity
from world.entities.human import Human 
from world.team import Team

class Player:
    def __init__(self):
        self.teams: List[Team] = []
        self.currentTeam: Team | None = None


