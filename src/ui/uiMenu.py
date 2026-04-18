from typing import Dict
from pygame import Rect, Vector2
from pygame_gui.core import UIElement
from pygame_gui.elements import UIButton

from enums.enumActionBasic import EnumActionBasic
from enums.enumActionMenu import EnumActionMenu
from ui.uiFactory import UIFactory


class UIMenu:

    def __init__(self, uiFactory: UIFactory):

        self.menuPanel = uiFactory.panel(Vector2(200, 200), Vector2(300, 300), "")
        self.menuLabel = uiFactory.label(Vector2(0, 0), Vector2(50, 15), "Menu", "Label", uiContainer=self.menuPanel)
        self.playButton  = uiFactory.button(Vector2(0, 0), Vector2(200, 50), "Go to world", "#playButton")

        self.uis = [
                self.menuLabel,
                self.playButton,
        ]

        self.actions: Dict[UIElement, EnumActionMenu | EnumActionBasic] = {
            self.playButton: EnumActionBasic.NAVIGATE_WORLD,
        }

    pass









