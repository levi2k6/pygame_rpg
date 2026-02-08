from pygame import Vector2, Surface

class Prop: 
    def __init__(self, name: str, position: Vector2, size: Vector2, sprite: Surface):
        self.name: str = name
        self.position: Vector2 = position 
        self.size: Vector2 = size
        self.sprite: Surface = sprite




