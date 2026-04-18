
from pygame import Rect, Vector2
from pygame.math import VectorElementwiseProxy
from pygame_gui import UIManager
from pygame_gui.core import IContainerLikeInterface, UIContainer, UIElement
from pygame_gui.elements import UILabel, UIButton, UIPanel  


class UIFactory:

    def __init__(self, uiManager: UIManager):
        self.uiManager = uiManager

    def label(
            self, 
            position: Vector2, 
            size: Vector2, 
            text: str, 
            objectId: str, 
            uiContainer: IContainerLikeInterface | None = None
    ):
        rect: Rect = Rect(position, size)
        return UILabel(relative_rect=rect, text=text, container=uiContainer, object_id=objectId, manager=self.uiManager)

    def button(self, position: Vector2, size: Vector2, text: str, objectId: str): 
        rect: Rect = Rect(position, size)
        return UIButton(relative_rect=rect, text=text, object_id=objectId, manager=self.uiManager)

     
    def panel(self, position: Vector2, size: Vector2, objectId: str):
        rect: Rect = Rect(position, size)
        return UIPanel(relative_rect=rect, object_id=objectId, manager=self.uiManager)
    pass

