from pygame import Rect, Vector2

from core.display import Display

class Camera:
    def __init__(self, display: Display):
        self.position: Vector2 = Vector2(0, 0)
        self.rect: Rect = Rect(0,0, display.width, display.height)





