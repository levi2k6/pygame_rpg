
from ui import uiFactory
from ui.uiFactory import UIFactory
from ui.uiMenu import UIMenu


class UIRegistry:

    def __init__(self, uiFactory: UIFactory):
        self.uiMenu: UIMenu = self.initUiWorld(uiFactory)
        pass

    def initUiWorld(self, uiFactory):
        return UIMenu(uiFactory)




