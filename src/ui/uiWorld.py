from pygame import Vector2
from inputs.inputFunction import InputFunction
from inputs.inputWorld import InputWorld
from ui.uiFactory import UIFactory


class UIWorld:

    def __init__(self, uiFactory: UIFactory, inputWorld: InputWorld):

        menuButton = uiFactory.button(Vector2(100, 30), Vector2(200, 50), "World", "#menuButton")

        self.uis = {
                menuButton: InputFunction("Navigate Menu", inputWorld.navigateMenu)
        }





