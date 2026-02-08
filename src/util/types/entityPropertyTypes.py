from pygame import Surface, Rect, Vector2

class CollisionBox: 
    __slots__ = {"boxRect", "position", "size"}

    def __init__(self, boxRect: Rect, position: Vector2, size: Vector2):
        self.boxRect: Rect = boxRect
        self.position: Vector2 = position
        self.size: Vector2 = size




