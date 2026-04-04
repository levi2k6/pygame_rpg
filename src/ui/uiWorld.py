from pygame import Vector2
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionWorld import EnumActionWorld
from ui.uiFactory import UIFactory


class UIWorld:

    def __init__(self, uiFactory: UIFactory):

        self.menuButton = uiFactory.button(Vector2(100, 30), Vector2(200, 50), "World", "#menuButton")
        self.worldTest = uiFactory.button(Vector2(100, 30), Vector2(100, 50), "World", "#worldTest")  

        self.uis = [
                self.menuButton
        ]

        self.actions = {
                self.menuButton: EnumActionBasic.NAVIGATE_MENU,
                self.worldTest: EnumActionWorld.TEST 
        }


