
from typing import Dict
from pygame import Rect, Vector2
from pygame_gui.core import UIElement
from pygame_gui.elements import UIButton

from enums.enumActionBasic import EnumActionBasic
from enums.enumActionCombat import EnumActionCombat
from enums.enumActionMenu import EnumActionMenu
from ui.uiFactory import UIFactory


class UICombat:

    def __init__(self, uiFactory: UIFactory):

        self.labelCombat = uiFactory.label(Vector2(300, 0), Vector2(200, 50), "Menu", "")
        self.attackButton  = uiFactory.button(Vector2(300, 30), Vector2(200, 50), "Attack", "#attackButton")

        self.uis = [
                self.labelCombat,
                self.attackButton,
        ]

        self.actions: Dict[UIElement, EnumActionCombat | EnumActionBasic] = {
            self.attackButton: EnumActionCombat.TEST,
        }

    pass

