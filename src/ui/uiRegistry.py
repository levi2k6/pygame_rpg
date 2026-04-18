
from pygame_gui import UIManager
from state.settings.display import Display
from ui.uiCombat import UICombat
from ui.uiFactory import UIFactory
from ui.uiMenu import UIMenu
from ui.uiWorld import UIWorld


class UIRegistry:

    def __init__(self, display: Display):
        self.uiManager = self.initUiManager(display)
        self.uiFactory = self.initUiFactory(self.uiManager) 
        self.uiMenu: UIMenu = self.initUiMenu(self.uiFactory)
        self.uiWorld: UIWorld = self.initUiWorld(self.uiFactory) 
        self.uiCombat: UICombat = self.initUiCombat(self.uiFactory)
        pass

    def  initUiManager(self, display: Display):
        width = display.screen.get_width()
        height = display.screen.get_height()
        return UIManager((width, height)) 

    def initUiFactory(self, uiManager: UIManager): 
        return UIFactory(uiManager) 

    def initUiMenu(self, uiFactory):
        return UIMenu(uiFactory)

    def initUiWorld(self, uiFactory):
        return UIWorld(uiFactory)

    def initUiCombat(self, uiFactory):
        return UICombat(uiFactory)


