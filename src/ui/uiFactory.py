
from pygame import Rect, Vector2
from pygame_gui.elements import UIButton
from core.uiManager import UIManager 


class UIFactory:

    def __init__(self, uiManager: UIManager):
        self.uiManager = uiManager


    def button(self, position: Vector2, size: Vector2, uiText: str): 
        rect: Rect = Rect(position, size)
        return UIButton(relative_rect=rect, text=uiText, manager=self.uiManager.manager)



    pass

