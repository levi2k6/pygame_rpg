
from pygame import Rect, Vector2
from pygame_gui.elements import UIButton

from inputs.inputFunction import InputFunction
from inputs.inputMenu import InputMenu
from ui.uiFactory import UIFactory


class UIMenu:

    def __init__(self, uiFactory: UIFactory, inputMenu: InputMenu):

        playButton = uiFactory.button(Vector2(30, 30), Vector2(200, 50), "Click", "#playButton") 
        testButton = uiFactory.button(Vector2(30, 100), Vector2(200, 50), "Click", "#testButton")

        self.uis = {
            playButton: InputFunction("Play game", inputMenu.playGame),
            testButton: InputFunction("Test", inputMenu.menuTest)
        }

    pass









