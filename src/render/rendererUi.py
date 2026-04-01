
from enum import Enum
from typing import List
from pygame import Event
from pygame_gui import UIManager

from Initialization.display import Display
from enums.enumScene import EnumScene
from init.coreRegistry import CoreRegistry
from ui.uiRegistry import UIRegistry


class RendererUI:
    def __init__(self, uiRegistry: UIRegistry, coreRegistry: CoreRegistry):
        self.uiManager = uiRegistry.uiManager 
        self.gameState = coreRegistry.gameState
        self.uiMenu = uiRegistry.uiMenu 

    def renderUi(self, uiManager: UIManager, display: Display, delta: float):
        uiManager.update(delta)
        uiManager.draw_ui(display.screen)

        if self.gameState.currentScene == EnumScene.MENU:
            self.uiMenu




        














