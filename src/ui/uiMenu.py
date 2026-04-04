
from pygame import Rect, Vector2
from pygame_gui.elements import UIButton

from enums.enumActionBasic import EnumActionBasic
from enums.enumActionMenu import EnumActionMenu
from ui.uiFactory import UIFactory


class UIMenu:

    def __init__(self, uiFactory: UIFactory):

        self.playButton  = uiFactory.button(Vector2(30, 30), Vector2(200, 50), "Click", "#playButton"),
        self.menuTest = uiFactory.button(Vector2(30, 100), Vector2(200, 50), "Click", "#menuTest")

        self.ations = {
            self.playButton: EnumActionBasic.NAVIGATE_WORLD,
            self.menuTest: EnumActionMenu.TEST
        }

    pass









