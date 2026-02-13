from typing import List
from pygame import Surface

from Entity.marker import Marker
from GameState.gameState import GameState
from Prop.prop import Prop

class Scene:
    def __init__(self):
        self.backgrounds: List[Surface] = []
        self.props: List[Prop] = []
        self.markers: List[Marker] = []



    def getMarker(self, name: str) -> Marker | None:
        for marker in self.markers:
            if marker.name == name:
                return marker
        return None

