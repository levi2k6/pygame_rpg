from typing import List
from pygame import Surface

from gameState.gameState import GameState
from Prop.prop import Prop

class Scene:
    def __init__(self):
        self.backgrounds: List[Surface] = []
        self.props: List[Prop] = []


