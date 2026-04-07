from pygame import Vector2
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionWorld import EnumActionWorld
from ui.uiFactory import UIFactory


class UIWorld:

    def __init__(self, uiFactory: UIFactory):

        self.worldLabel = uiFactory.label(Vector2(10, 0), Vector2(200, 50), "World", "")
        self.menuButton = uiFactory.button(Vector2(10, 30), Vector2(200, 50), "Go to Menu", "#menuButton")

        self.uis = [
                self.worldLabel,
                self.menuButton
        ]

        self.actions = {
                self.menuButton: EnumActionBasic.NAVIGATE_MENU,
        }


