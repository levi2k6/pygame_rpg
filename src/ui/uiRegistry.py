
from pygame_gui import UIManager
from Initialization.display import Display
from inputs.inputMenu import InputMenu
from inputs.inputRegistry import InputRegistry
from inputs.inputWorld import InputWorld
from ui.uiFactory import UIFactory
from ui.uiMenu import UIMenu
from ui.uiWorld import UIWorld


class UIRegistry:

    def __init__(self, display: Display, inputRegistry: InputRegistry):
        self.uiManager = self.initUiManager(display)
        self.uiFactory = self.initUiFactory(self.uiManager) 
        self.uiMenu: UIMenu = self.initUiMenu(self.uiFactory, inputRegistry.inputMenu)
        self.uiWorld: UIWorld = self.initUiWorld(self.uiFactory, inputRegistry.inputWorld) 
        pass

    def  initUiManager(self, display: Display):
        return UIManager((display.width, display.height)) 

    def initUiFactory(self, uiManager: UIManager): 
        return UIFactory(uiManager) 

    def initUiMenu(self, uiFactory, inputMenu: InputMenu):
        return UIMenu(uiFactory, inputMenu)

    def initUiWorld(self, uiFactory, inputWorld: InputWorld):
        return UIWorld(uiFactory, inputWorld)



