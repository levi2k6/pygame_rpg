from pygame import Rect, Vector2

from state.settings.display import Display

class Camera:
    def __init__(self, display: Display):
        self.position: Vector2 = Vector2(0, 0)
        self.rect: Rect = Rect(0,0, display.screen.get_width(), display.screen.get_height())





