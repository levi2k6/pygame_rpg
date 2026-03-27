


from typing import List
from pygame import Rect, Vector2


class UI: 
    def __init__(self, position: Vector2, rect: Rect):
        self.position = position 
        self.rect = rect 
        self.parent: UI =  ui
        self.children: List[UI] = []
        pass



