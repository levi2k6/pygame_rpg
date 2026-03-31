
from pygame import Rect, Vector2
from pygame_gui.elements import UIButton

from ui.uiFactory import UIFactory


class UIMenu:

    def __init__(self, uiFactory: UIFactory):
        self.playButton: UIButton = uiFactory.button(Vector2(30, 30), Vector2(200, 50), "Click") 


    pass









